from django.http import request
from django.shortcuts import render
from .models import User, UserDetail,UserImage
from django.utils import timezone
from django.shortcuts import render,redirect
from django.views import generic
from .forms import PostForm,LoginForm,UpLoadProfileImgForm
from django.urls import reverse_lazy

model = User

# トップ画面を表示
class TopView(generic.TemplateView):
    
    def topDispView(request):
        
        # セッション確認
        if 'user_id' in request.session:
            return render(request,'matching/top.html', {'error': "セッション有"})

        else:
            return render(request,'matching/top.html', {'error': "セッション無"})

     
# ログイン画面を表示
class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'matching/login.html'

    # ログイン画面を開いたときに、セッション取得できない場合は、別画面にリダイレクトする
    def dispatch(self, request, *args, **kwargs):
        if 'user_id' in request.session:
            session_id = request.session.get('user_id')
            data = model.objects.get(user_id=session_id)
            return render(request,'matching/login_success.html', {'data': data})
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return render(request,'matching/login')
    
# ログアウト画面を表示
class LogoutView(generic.TemplateView):
    
    def logout(request):
        request.session.clear()
        return render(request,'matching/logout.html')


# ログイン処理＋ログイン画面遷移
class LoginSuccessView(generic.FormView):

    def login(request):

        session_id = request.session.get('user_id')
        if  session_id :
            data = model.objects.get(user_id=session_id)
            return render(request,'matching/login_success.html', {'data': data})
        
        
        # POSTで受け取ったデータからユーザーIDとパスワードを取得
        id = request.POST.get('user_id')
        password = request.POST.get('user_password')

        try:
            
            # ユーザーIDの存在チェックを行う
            # ユーザーのデータを変数に格納
            model.objects.get(user_id=id)
            data = model.objects.get(user_id=id)

            # パスワードチェック
            if data.user_password == password:
                #ログイン成功
                #セッションにログイン情報を設定
                request.session['user_id']=id

                # クッキーに保存
                template = 'matching/login.html'
                context = {'data': data}
                response = render(request, template, context)
                response.set_cookie('key', 'value')
                return render(request,'matching/login_success.html', {'data': data})
            else:
                # ログイン失敗
                return render(request,'matching/top.html', {'error': 'パスワードが間違ってます'})
        except model.DoesNotExist:
            # モデルから入力されたIDのデータが取得できなかった場合
            return render(request,'matching/top.html', {'error': '存在しないIDです。'})
        except:
            # 想定外のエラー
            return render(request,'matching/top.html', {'error': '予期せぬエラーが発生しました'})


# アカウント作成フォーム+実行処理
# アカウント作成成功後、ログイン画面に遷移する。
class CreateAccountView (generic.CreateView):
    form_class = PostForm
    model = User     
    template_name = 'matching/create_account.html'
    success_url = reverse_lazy('login')

class ChatView(generic.TemplateView):
    
    # template_name = 'matching/chat.html'

    # ログイン画面を開いたときに、セッション取得できない場合は、別画面にリダイレクトする
    def dispatch(self, request, *args, **kwargs):
        if 'user_id' not in request.session:
            return render(request,'matching/top.html', {'error': '予期せぬエラーが発生しました'})
        else:
            session_id = request.session.get('user_id')
            data = model.objects.get(user_id=session_id)
            return render(request,'matching/chat.html', {'data': data})
            

class ProfileView(generic.FormView):
    
    def profile(request):
        
        if request.method == 'POST':
            form = UpLoadProfileImgForm(request.POST, request.FILES)
        else:
            form = UpLoadProfileImgForm()
        
        image_model = UserImage
        session_id = request.session.get('user_id')

        if form.is_valid():
            avator = form.cleaned_data['user_images']
            image = UserImage()
            image.user_images = avator
            image.user_id = session_id
            image.save()

            UserDetail.objects.update_or_create(
                user_id = session_id,
                defaults={
                    "user_name": form.cleaned_data['user_name'], 
                    "user_profile": form.cleaned_data['user_profile']  
                }
            )
            
        data = image_model.objects.filter(user_id=session_id)
        return render(request, 'matching/profile.html', {'form': form ,'image':data})

class UserListView(generic.TemplateView):

    def display_list_view(request):

        session_id = request.session.get('user_id')
        user_detail_model = UserDetail
        user_image_model = UserImage
        detail_data = user_detail_model.objects.exclude(user_id=session_id)
        len(detail_data)
        image_data = user_image_model.objects.exclude(user_id=session_id)

        return render(request, 'matching/user_list.html', {'detail': detail_data ,'image':image_data})
