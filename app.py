#!/usr/bin/env python3
"""A simple application to demo Thoth's software stack recommendations."""

import sys
import tensorflow as tf

from flask import Flask


app = Flask(__name__)


def terminal_hello_v1():
    """Print hello world from within a TensorFlow session."""
    hello = tf.constant("Hello Thoth, your friend TensorFlow v1!")
    sess = tf.Session()
    print(sess.run(hello))


def terminal_hello_v2():
    """Print hello world from within a TensorFlow session."""
    hello = tf.constant("Hello Thoth, your friend TensorFlow v2!")
    tf.print(hello)


@app.route("/v2")
def flask_hello_v2():
    return "Hello Thoth, your friend TensorFlow v2!"


if __name__ == "__main__":
    tf_version = tf.__version__
    if int(tf_version[0]) >= 2:
        terminal_hello_v2()
    else:
        terminal_hello_v1()

    app.run(port=8080, host="0.0.0.0")

