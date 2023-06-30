# The MIT License (MIT)
# Copyright © 2023 Yuma Rao

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import time
import argparse
import bittensor as bt

from typing import Optional
from .base_miner.miner import BaseMiner
from .protocol import DummyRequest, DummyResponse

class DummyMiner( BaseMiner ):

    def forward( self, request: DummyRequest ) -> DummyResponse:
        return DummyResponse( dummy = request.dummy )

    @classmethod
    def add_args(cls, parser: argparse.ArgumentParser):
        parser.add_argument("--dummy.argument", type=str, help="Dummy argument")

    def __init__(self, api_key: Optional[str] = None, *args, **kwargs):
        super ( DummyMiner, self ).__init__(*args, **kwargs)
        print ( self.config )
        print ( self.config.dummy.argument )

if __name__ == "__main__":
    with DummyMiner():
        while True:
            print( "running...", time.time() )
            time.sleep(1)


