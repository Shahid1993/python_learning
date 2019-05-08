from loguru import logger
import sys


"""Easier file logging with rotation / retention / compression"""

logger.debug("That's it, beautiful and simple logging!")
logger.add("file_{time}.log")

logger.add("file_1.log", rotation="500 MB")    # Automatically rotate too big file
logger.add("file_2.log", rotation="12:00")     # New file is created each day at noon
logger.add("file_3.log", rotation="1 week")    # Once the file is too old, it's rotated

logger.add("file_X.log", retention="10 days")  # Cleanup after some time

logger.add("file_Y.log", compression="zip")    # Save some loved space

logger.info("testing...")

"""Modern string formatting using braces style"""

logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")

"""Exceptions catching within threads or main"""

@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)

my_function(0,0,0)

"""Pretty logging with colors"""

logger.add(sys.stdout, colorize=True, format="<red>{time}</red> <level>{message}</level>")
logger.info("testing...0000000000000")

"""Asynchronous, Thread-safe, Multiprocess-safe"""

logger.add("somefile.log", enqueue=True)


""" Fully descriptive exceptions """

#logger.add("output.log", backtrace=True, diagnose=True)  # Set 'False' to not leak sensitive data in prod
logger.add("output.log", backtrace=True)
def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)

def custom_sink_function(obj):
	print (obj)

def expensive_function(obj):
	print (obj)

"""Structured logging as needed"""
logger.add(custom_sink_function, serialize=True)

logger.add("file.log", format="{extra[ip]} {extra[user]} {message}")
logger_ctx = logger.bind(ip="192.168.0.1", user="someone")
logger_ctx.info("Contextualize your logger easily")
logger_ctx.bind(user="someoneelse").info("Inline binding of extra attribute")

logger.add("special.log", filter=lambda record: "special" in record["extra"])
logger.debug("This message is not logged to the file")
logger.bind(special=True).info("This message, though, is logged to the file!")

"""Lazy evaluation of expensive functions"""

logger.opt(lazy=True).debug("If sink level <= DEBUG: {x}", x=lambda: expensive_function(2**64))

# By the way, "opt()" serves many usages
logger.opt(exception=True).info("Error stacktrace added to the log message")
logger.opt(ansi=True).info("Per message <blue>colors</blue>")
logger.opt(record=True).info("Display values from the record (eg. {record[thread]})")
logger.opt(raw=True).info("Bypass sink formatting\n")
logger.opt(depth=0).info("Use parent stack context (useful within wrapped functions)")


"""Customizable levels"""
new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")

logger.log("SNAKY", "Here we go!")


"""Better datetime handling"""
logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")


"""Suitable for scripts and libraries"""
# For scripts
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": "file.log", "serialize": True},
    ],
    "extra": {"user": "someone"}
}
logger.configure(**config)

# For libraries
logger.disable("my_library")
logger.info("No matter added sinks, this message is not displayed")
logger.enable("my_library")
logger.info("This message however is propagated to the sinks")

