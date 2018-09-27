#!/bin/bash

uname -a
free -m
df -h
ulimit -a
mkdir builds
pushd builds

# Build into own virtualenv
# We therefore control our own environment, avoid travis' numpy
pip install -U virtualenv

if [ -n "$USE_DEBUG" ]
then
  virtualenv --python=python3-dbg venv
else
  virtualenv --python=python venv
fi

source venv/bin/activate
python -V

VERSION=$(python -c "import sys; print(sys.version[:3])")
if [ "$VERSION" == "3.7" ]; then
  # use pickle5 backport when on python3.7
  pip install pickle5
fi

pip install --upgrade pip setuptools
pip install nose pytz cython pytest
if [ -n "$USE_ASV" ]; then pip install asv; fi
popd
