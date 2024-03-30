#!/bin/bash
# takes a URL, sends a request, and displays size of the response
curl -sX GET $1 -L
