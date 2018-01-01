'''
    NEM NIS
    -------

    Low-level API wrapper NEM RESTful GET requests to aysnchronous
    futures sharing a client session. Provides a 1-1 translation
    of NEM RESTful Requests to wrapper methods, returning futures
    for each request.

    Please see the NEM documentation for documentation on the REST
    API functionality encapsulated by this wrapper:
        https://bob.nem.ninja/docs

    For information on how to use the Simple REST-generated API,
    please see:
        https://github.com/Q-chain/python-simple-rest

    A list of public NEM nodes can be found here:
        https://supernodes.nem.io/

    .. code-block:: python
        >>> import nis
        >>> address = # add address here, for example 'http://176.9.68.110:7890'
        >>> rest = nis.Api(address=address)
        >>> rest._run(rest.heartbeat())
        {'code': 1, 'message': 'ok', 'type': 2}
        >>> rest._run(rest.status())
        {'code': 6, 'message': 'status', 'type': 4}
        >>> rest._run(rest.chain.height())
        {'height': 1441112}
        >>> rest._run(rest.chain.score())
        {'score': '07dcf15eae8d382702'}
'''

import os
import rest

__all__ = ['Api']

# API
# ---

HOME = os.path.dirname(os.path.realpath(__file__))
API_JSON = os.path.join(HOME, 'api.json')
Root = rest.Root.from_json(open(API_JSON, 'r').read())
Api = rest.factory("Api",  Root)
