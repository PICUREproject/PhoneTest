import webbrowser
import http.server
import socketserver


PORT = 8000

html_content = '''
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>socialLogin</title>
    <link rel="icon" href="data:,">
  </head>
  <body>
    <button id="googleLogin">구글 아이디로 로그인</button>
    <form>
      핸드폰 번호 : <input id="phoneNumber" />
      <button id="phoneNumberButton">핸드폰 번호 전송</button>
    </form>
    <form>
      확인 코드 : <input id="confirmCode" />
      <button id="confrimCodeButton">확인 코드 전송</button>
    </form>
    <script type="module">
      // Import the functions you need from the SDKs you need
      import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.2/firebase-app.js";
      import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.9.2/firebase-analytics.js";
      import {
        getAuth,
        signInWithPopup,
        GoogleAuthProvider,
        signInWithPhoneNumber,
        RecaptchaVerifier,
      } from "https://www.gstatic.com/firebasejs/9.9.2/firebase-auth.js";

      // TODO: Add SDKs for Firebase products that you want to use
      // https://firebase.google.com/docs/web/setup#available-libraries

      // Your web app's Firebase configuration
      // For Firebase JS SDK v7.20.0 and later, measurementId is optional
      const firebaseConfig = {
        apiKey: "AIzaSyCH_qQKgvX04MCiInM0t-1el2gXoNc9YpI",
        authDomain: "easylogin-69172.firebaseapp.com",
        projectId: "easylogin-69172",
        storageBucket: "easylogin-69172.appspot.com",
        messagingSenderId: "507786873248",
        appId: "1:507786873248:web:a4effc2440a8e81bfbfcc5",
        measurementId: "G-X3G15GWG5T",
      };

      // Initialize Firebase
      const app = initializeApp(firebaseConfig);
      const analytics = getAnalytics(app);

      const provider = new GoogleAuthProvider();
      const auth = getAuth();
      auth.languageCode = "ko";

      document.getElementById("googleLogin").addEventListener("click", () => {
        signInWithPopup(auth, provider)
          .then((result) => {
            // This gives you a Google Access Token. You can use it to access the Google API.
            const credential = GoogleAuthProvider.credentialFromResult(result);
            const token = credential.accessToken;
            // The signed-in user info.
            const user = result.user;
            console.log(result);
            // ...
          })
          .catch((error) => {
            // Handle Errors here.
            const errorCode = error.code;
            const errorMessage = error.message;
            // The email of the user's account used.
            const email = error.customData.email;
            // The AuthCredential type that was used.
            const credential = GoogleAuthProvider.credentialFromError(error);
            console.log(error);
            // ...
          });
      });
      window.recaptchaVerifier = new RecaptchaVerifier(
        "phoneNumberButton",
        {
          size: "invisible",
          callback: (response) => {
            // reCAPTCHA solved, allow signInWithPhoneNumber.
            onSignInSubmit();
          },
        },
        auth
      );

      document
        .getElementById("phoneNumberButton")
        .addEventListener("click", (event) => {
          event.preventDefault();

          const phoneNumber = document.getElementById("phoneNumber").value;
          const appVerifier = window.recaptchaVerifier;

          signInWithPhoneNumber(auth, "+82" + phoneNumber, appVerifier)
            .then((confirmationResult) => {
              // SMS sent. Prompt user to type the code from the message, then sign the
              // user in with confirmationResult.confirm(code).
              window.confirmationResult = confirmationResult;
              console.log(confirmationResult);
              // ...
            })
            .catch((error) => {
              console.log(error);
              // Error; SMS not sent
              // ...
            });
        });

      document
        .getElementById("confrimCodeButton")
        .addEventListener("click", (event) => {
          event.preventDefault();
          const code = document.getElementById("confirmCode").value;
          confirmationResult
            .confirm(code)
            .then((result) => {
              // User signed in successfully.
              const user = result.user;
              console.log(result);
              // ...
            })
            .catch((error) => {
              console.log(error);
              // User couldn't sign in (bad verification code?)
              // ...
            });
        });
    </script>
  </body>
</html>
'''

num = int(input("숫자를 입력하세요: "))

# 조건을 체크합니다.

if num % 2 == 0:
        print(1)
        with open('social_login.html', 'w', encoding='utf-8') as file:
          file.write(html_content)

        # 기본 웹 브라우저에서 HTML 파일을 엽니다.
        class Handler(http.server.SimpleHTTPRequestHandler):
              
          def end_headers(self):
              self.send_header('Access-Control-Allow-Origin', '*')
              http.server.SimpleHTTPRequestHandler.end_headers(self)

        # 현재 디렉토리에서 HTTP 서버를 시작합니다.
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            webbrowser.open(f"http://localhost:{PORT}/social_login.html")
            httpd.serve_forever()
        webbrowser.open('message.html')

        
else:
        print(0)

