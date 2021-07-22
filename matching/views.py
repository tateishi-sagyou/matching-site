from django.http import request
from django.shortcuts import render
from .models import User
from django.utils import timezone
from django.shortcuts import render
from django.views import generic
from .forms import PostForm,LoginForm
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
            # return super().dispatch(request, *args, **kwargs)
            




# *************************************************
# これで一応動きます
# *************************************************
# class CreateAccountView (generic.FormView):
#     form_class = PostForm      
#     template_name = 'login/create_account.html'

# class ExecCreateAccount (generic.CreateView):
#     model = Login
#     form_class = PostForm      
#     template_name = 'login/create_account_success.html'

# *************************************************

    # success_url = 'login/create_account_success.html'

    # def get_success_url(self,request):
    #     id = self.object.id

    #     return render(request, 'login/create_account_success.html',{
    #         'id':id
    #     }


    # def get_success_url(self):
        # return reverse('create_done', kwargs={'pk': self.object.id})


    # success_url = reverse_lazy('login/create_account_success.html')
    # def get_success_url(self):
    #     return reverse('create_done1', kwargs={'pk': self.object.id})

    # def execCreate(request):
    #     id = request.POST.get('user_id')
    #     password = request.POST.get('user_password')
    #     return render(request, 'login/create_account_success.html',{
    #         'id':id
    #     })





#  class CreateAccountView(generic.CreateView):
#     form_class = PostForm
#     template_name = 'login/create_account.html'
#     # success_url = reverse_lazy('create_done')
#     # success_url = '/login/create_account_success.html'  # 成功時にリダイレクトするURL
#     success_url = reverse_lazy('create_done', kwargs={'pk': model.object.id})
#     # def get_success_url(self):
#     #     return reverse('create_done', kwargs={'pk': self.object.id})
#     def get_success_url(self):
#         data = self.object.id
#         return render(request, 'login/create_account_success.html',{
#             'data':data
#         })
        
    # def create_done(request, **kwargs):
    #     contents = {}
    #     for key, val in kwargs.items():
    #         contents[key] = val

    #     userinfoDetail = get_object_or_404(Login,pk=kwargs.get('pk'))
    #     data = {
    #         'userinfoDetail':userinfoDetail,
    #     }

    #     return render(request, 'login/create_account_success.html',{
    #         'contents': contents ,'data':data
    #     })
