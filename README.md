![stapler](/public/static/stapler.png)

# Case of the Mondays

A team-building application.

If you're unfamiliar with the reference, check out 
[this](https://www.youtube.com/watch?v=uiik3zS4y4I) and
[this](https://www.youtube.com/watch?v=Q77nwCUc6lk). Basically, my manager
wanted help with a virtual team-builder, and I've always wanted to learn about
web development, so... here we are.

It's a bare-bones setup meant to be hosted on a laptop or development system.
The only thing you need is Python. It's intended to be run in a very ad-hoc
fashion from within the repository itself. Team-builders don't need fancy
things.

> [!NOTE]
> I've only tested on Windows, but I'm pretty sure it will work in other
> environments as well (minus the front-end BAT script).

## How to start the server

Clone the repository.
```sh
git clone https://github.com/newtonian/cotm
cd cotm
```

Run the initialization script.
```sh
cotm init
```

Start the server.
```sh
cotm server [--host name] [--port num]
```

You should see the following output:
```
          )            *     
   (   ( /(   *   )  (  `    
   )\  )\())` )  /(  )\))(   
 (((_)((_)\  ( )(_))((_)()\  
 )\___  ((_)(_(_()) (_()((_) 
((/ __|/ _ \|_   _| |  \/  | 
 | (__| (_) | | |   | |\/| | 
  \___|\___/  |_|   |_|  |_|
     CASE OF THE MONDAYS

Server is RUNNING

http://localhost:8888          [Players]
http://localhost:8888/screen   [Projector]
http://localhost:8888/console  [Admin]

Press CTRL+C to exit...
```

At this point, in web browsers:
* Direct your team to the player URL.
* Share your screen and go to the projector URL.
* Use the console URL to administer the server.
