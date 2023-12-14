r"""
          )            *     
   (   ( /(   *   )  (  `    
   )\  )\())` )  /(  )\))(   
 (((_)((_)\  ( )(_))((_)()\  
 )\___  ((_)(_(_()) (_()((_) 
((/ __|/ _ \|_   _| |  \/  | 
 | (__| (_) | | |   | |\/| | 
  \___|\___/  |_|   |_|  |_|
     CASE OF THE MONDAYS
"""

import os
from socket import gethostname
import time
from textwrap import dedent
from threading import Thread
import traceback

import bottle
import click

from cotm import log
from cotm import routes
from cotm.log import green

__all__ = [ routes ]  # Solves unused import warning

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

PROG_NAME = "cotm"


def start_server(host: str, port: int, debug_: bool, loud: bool) -> None:
    """Kick off thread for web server

    There is a weird issue with pressing CTRL+C to exit the bottle.run method.
    (ResourceWarning unclosed <socket.socket>...). I worked around it by running
    it in a separate thread and then monitoring the keyboard interrupt on the
    main thread.
    """
    log.debug("Starting bottle thread")
    Thread(
        target=bottle.run,
        kwargs={"host": host, "port": port, "debug": debug_, "quiet": not loud},
    ).start()


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("--host", help="HTTP hostname/ip", default=gethostname())
@click.option("--port", help="HTTP port", type=int, default=8888)
@click.option("--debug", help="Enable debug logging", is_flag=True)
@click.option("--loud", help="Log each HTTP request", is_flag=True)
def main(
    host: str = None,
    port: int = None,
    debug: bool = None,
    loud: bool = None,
) -> None:
    """Start cotm server"""
    log.debug_on = debug

    # Print logo
    print(green(__doc__))

    start_server(host, port, debug, loud)

    base_url = f"http://{host}:{port}"

    print(
        dedent(
            f"""\
            Server is {green('RUNNING')}

            {base_url}          [{green('Players')}]
            {base_url}/screen   [{green('Projector')}]
            {base_url}/console  [{green('Admin')}]

            Press CTRL+C to exit...
            """
        )
    )

    try:
        while True:
            time.sleep(0xffffffff)
    except KeyboardInterrupt:
        print("Goodbye")
    except Exception:
        # If we don't catch everything, the process won't exit
        traceback.print_exc()
    finally:
        os._exit(0)


if __name__ == "__main__":
    main(prog_name=PROG_NAME)
