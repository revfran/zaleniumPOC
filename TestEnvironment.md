    # Pull docker-selenium
    docker pull elgalu/selenium:3.141.59-p8
    
    # Pull Zalenium
    docker pull dosel/zalenium:3.141.59g
    
    # Run it!
    docker run --rm -ti --name zalenium -p 4444:4444 \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v /tmp/videos:/home/seluser/videos \
      --privileged dosel/zalenium:3.141.59g start
      
    # Point your tests to http://localhost:4444/wd/hub and run them

    # Stop
    docker stop zalenium
