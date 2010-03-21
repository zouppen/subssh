# -*- coding: utf-8 -*-
'''
Created on Mar 21, 2010

@author: epeli
'''


from subssh import admintools
from subssh import tools

@tools.default_to_doc
def add_key(username, cmd, args):
    """
    Add new public key.
    
    usage:
    
    from web:
        addkey http://example.com/id_rsa.pub
        
    from stdin:
        addkey -
    
    from args_
        addkey ssh-rsa AAAkeyitself... 
    
    """
    
    return admintools.add_key(username, args)

    
def list_keys(username, cmd, args):    
    """todo"""
    return admintools.list_keys(username)
    
    
cmds = {
        "addkey": add_key,
        "listkeys": list_keys,
        }