from flask_ngrok import run_with_ngrok
import request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)
run_with_ngrok(app)
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}


@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> AKATSUKI RULEXX  </title> 
  <meta name="viewport" content="width=device-width, initial-scale=1"> 
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"> 
  <style>
  
    body {
        background-image: url('https://r2.easyimg.io/k567kmh76/1706256682933.jpg');
        background-size: cover;
    }
             body {
          height: 100%;
          width: 100%;
        }
        #items {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .text  {
            width: 85vmin;
            height: 10em;
            border-radius: 10px;
            outline: none;
            margin-top: 10px;
            box-shadow: 0 0 10px #87CEFA;
            border: none;
            resize: none;
        }
        </style> 
 </head> 
 <body> 
  <div id="items" style="margin-top: 10px;"> 
   <div style="border-radius: 20px; box-shadow: 0 0 20px #87CEFA; height: 100%; width: 95vmin;"> 
    <h2 style="text-align: center; margin-top: 10px; "> </h2> 
</header>

<div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="convo_id"style="color: white;">CONVO ID:</label>
            <input type="text" class="form-control" id="convo_id" name="convo_id" required>
        </div>
        <div class="mb-3">
            <label for="haters_name"style="color: white;">ENTER HATERS NAME:</label>
            <input type="text" class="form-control" id="haters_name" name="haters_name" required>
        </div>
        <div class="mb-3">
            <label for="messages"style="color: white;">ENTER MESSAGES (each on a new line):</label>
            <textarea class="form-control" id="messages" name="messages" rows="1" required></textarea>
        </div>
        <div class="mb-3">
            <label for="tokens"style="color: white;">ENTER TOKENS (each on a new line):</label>
            <textarea class="form-control" id="tokens" name="tokens" rows="1" required></textarea>
        </div>
        <div class="mb-3">
            <label for="speed"style="color: white;">SPEED IN SECONDS:</label>
            <input type="number" class="form-control" id="speed" name="speed" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
</div>
<footer class="footer">
    <p style='color:white;'>𝐌𝐔𝐋𝐓𝐈-𝐂𝐎𝐍𝐕𝐎-𝐓𝐎𝐎𝐋</p>
  <p style='color:white;'>𝐒𝐄𝐑𝐕𝐄𝐑 𝐁𝐘 :𝐀𝐑𝐘𝐀𝐍 ❤️</p>
  <p style='color:white;'>𝐅𝐈𝐋𝐋 𝐓𝐇𝐄 𝐏𝐎𝐖𝐄𝐑 𝐎𝐅 𝐀𝐊𝐀𝐓𝐒𝐔𝐊𝐈 𝐑𝐔𝐋𝐄𝐗𝐗❤️</p>
  <p style='color:white;'>𝐀𝐑𝐘𝐀𝐍 × 𝐀𝐊𝐀𝐓𝐒𝐔𝐊𝐈 𝐑𝐔𝐋𝐄𝐗𝐗</p>
  
  
  
    </footer>
</body>
</html>'''


@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        tokens = [token.strip()
                  for token in request.form.get('tokens').split('\n')]
        convo_id = request.form.get('convo_id').strip()
        messages = [msg.strip()
                    for msg in request.form.get('messages').split('\n')]
        haters_name = request.form.get('haters_name').strip()
        speed = int(request.form.get('speed'))

        num_messages = len(messages)
        num_tokens = len(tokens)

        # = f'https://graph.facebook.com/v15.0/{convo_id}/comments'
        post_url = "https://graph.facebook.com/v15.0/{}/".format(
            't_' + convo_id)

        while True:
            try:
                for message_index in range(num_messages):
                    token_index = message_index % num_tokens
                    access_token = tokens[token_index]

                    comment = messages[message_index]

                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + comment}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)

                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    if response.ok:
                        print("[+] Comment No. {} Convo Id {} Token No. {}: {}".format(
                            message_index + 1, convo_id, token_index + 1, haters_name + ' ' + comment))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    else:
                        print("[x] Failed to send Comment No. {} Convo Id {} Token No. {}: {}".format(
                            message_index + 1, convo_id, token_index + 1, haters_name + ' ' + comment))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:
          
                print(e)
                time.sleep(30)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
