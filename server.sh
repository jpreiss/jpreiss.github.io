echo "go to" `ipconfig getifaddr en0`:8888
python3 -m http.server 8888 --bind 0.0.0.0
