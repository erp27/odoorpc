# -*- coding: UTF-8 -*-
##############################################################################
#
#    OdooRPC
#    Copyright (C) 2014 Sébastien Alix.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
"""This module contains all exceptions raised by `OdooRPC` when an error
occurred.
"""


class Error(Exception):
    """Base class for exception."""
    pass


class RPCError(Error):
    """Exception raised for errors related to RPC queries.
    Error details (like the `Odoo` server traceback) are available through the
    `info` attribute:

        >>> from pprint import pprint as pp
        >>> try:
        ...     odoo.execute('res.users', 'wrong_method')
        ... except odoorpc.error.RPCError as exc:
        ...     pp(exc.info)
        ...
        {'code': 200,
         'data': {'arguments': ["'res.users' object has no attribute 'wrong_method'"],
                  'debug': 'Traceback (most recent call last):\\n  File "/home/odoo/odoo/server/openerp/http.py", line 499, in [...]',
                  'message': "'res.users' object has no attribute 'wrong_method'",
                  'name': 'exceptions.AttributeError'},
         'message': 'OpenERP Server Error'}
    """
    def __init__(self, message, info=False):
        super(Error, self).__init__(message, info)
        self.info = info

    def __str__(self):
        return self.args and self.args[0] or ''

    def __repr__(self):
        return "%s(%s)" % (
            self.__class__.__name__,
            repr(self.args[0]))


class LoginError(Error):
    """Exception raised when the login on a server has failed."""
    pass


class InternalError(Error):
    """Exception raised for errors occurring during an internal operation."""
    pass

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
