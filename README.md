[![Build Status](https://travis-ci.org/xinitrc-ls/prettytwitch.svg?branch=master)](https://travis-ci.org/xinitrc-ls/prettytwitch) 

'Pretty Twitch' library
=======================
This library allows you to identify any **Twitch IRC** server response and format it to your liking!

Installing
----------

```sh

  pip install prettytwitch
```

Recieving pretty responses
--------------------------
Beforehand: Grab your OAuth token here: https://twitchapps.com/tmi/


```python

  from prettytwitch import Response  # importing library
  
  import socket
  from time import sleep

  NICK = 'Your username'
  PASS = 'your twitch OAuth token'
  CHAN = '#channel_name'
  
  RATE = (20/30)  # Rate per socket established by Twitch

  s = socket.socket()
  s.connect(('irc.chat.twitch.tv', 6667))
  s.send("CAP REQ :twitch.tv/commands\r\n".encode())  # Next too lines allows you to recieve more data with
  s.send("CAP REQ :twitch.tv/tags\r\n".encode())      # your client; you can find more info at dev.twitch.tv
  s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
  s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
  s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

  # Getting the information and correctly (line by line) sending it to the library to "pretify"
  # Reason for this mess is that because of the ratelimit we can get certain data in chunks,
  # and sometimes those chunks might not be complete, example gratia:
  # ThisIsLine1\r\nThisIsLine2\r\nThisIsLi

  leftovers = ''
  while True:
      raw_responses = s.recv(1024).decode("utf-8")

      if leftovers != '':
          raw_responses = leftovers + raw_responses
          leftovers = ''

      responses = [r+'\r\n' for r in raw_responses.strip().split('\r\n') if r]
      if not raw_responses.endswith('\r\n'):
          leftovers = responses[-1][:-2]
          responses = responses[:-1]

      for response in responses:
          # print(response)
          print(Response(response))

      sleep(1 / RATE)
```

Next steps
----------

Did I get you interested? Make sure to check the [wiki on GitHub](https://github.com/xinitrc-ls/prettytwitch/wiki) for documentation, examples, and more useful information.
