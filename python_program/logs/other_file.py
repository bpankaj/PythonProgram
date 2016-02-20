#soumiyajit
	from oslo_log import log as logging
	from heat.common.i18n import _LE
	from heat.common.i18n import _LI
	LOG = logging.getLogger(__name__)#soumiyajit
	from oslo_log import log as logging
	from heat.common.i18n import _LE
	from heat.common.i18n import _LI
	LOG = logging.getLogger(__name__)#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import collections
import itertools

from oslo_serialization import jsonutils
import six

from heat.api.aws import utils as aws_utils
from heat.common import exception
from heat.common.i18n import _
from heat.engine import function
from heat.engine import resource


class FindInMap(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap "))
    '''
    A function for resolving keys in the template mappings.

    Takes the form::

        { "Fn::FindInMap" : [ "mapping",
                              "key",
                              "value" ] }
    '''

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap/ __init__ "))
        super(FindInMap, self).__init__(stack, fn_name, args)

        try:
            self._mapname, self._mapkey, self._mapvalue = self.args
        except ValueError as ex:
            raise KeyError(six.text_type(ex))

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class FindInMap/ result "))
        mapping = self.stack.t.maps[function.resolve(self._mapname)]
        key = function.resolve(self._mapkey)
        value = function.resolve(self._mapvalue)
        return mapping[key][value]


class GetAZs(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAZs "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAZs "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAZs "))
    '''
    A function for retrieving the availability zones.

    Takes the form::

        { "Fn::GetAZs" : "<region>" }
    '''

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAZs/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAZs/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAZs/ result "))
        # TODO(therve): Implement region scoping
        # region = function.resolve(self.args)

        if self.stack is None:
            return ['nova']
        else:
            return self.stack.get_availability_zones()


class ParamRef(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef "))
    '''
    A function for resolving parameter references.

    Takes the form::

        { "Ref" : "<param_name>" }
    '''

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef/ __init__ "))
        super(ParamRef, self).__init__(stack, fn_name, args)

        self.parameters = self.stack.parameters

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ParamRef/ result "))
        param_name = function.resolve(self.args)

        try:
            return self.parameters[param_name]
        except KeyError:
            raise exception.InvalidTemplateReference(resource=param_name,
                                                     key='unknown')


class ResourceRef(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef "))
    '''
    A function for resolving resource references.

    Takes the form::

        { "Ref" : "<resource_name>" }
    '''

    def _resource(self, path='unknown'):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ _resource "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ _resource "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ _resource "))
        resource_name = function.resolve(self.args)

        try:
            return self.stack[resource_name]
        except KeyError:
            raise exception.InvalidTemplateReference(resource=resource_name,
                                                     key=path)

    def dependencies(self, path):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ dependencies "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ dependencies "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ dependencies "))
        return itertools.chain(super(ResourceRef, self).dependencies(path),
                               [self._resource(path)])

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceRef/ result "))
        return self._resource().FnGetRefId()


def Ref(stack, fn_name, args):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/ Ref "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/ Ref "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/ Ref "))
    '''
    A function for resolving parameters or resource references.

    Takes the form::

        { "Ref" : "<param_name>" }

    or::

        { "Ref" : "<resource_name>" }
    '''
    if args in stack:
        RefClass = ResourceRef
    else:
        RefClass = ParamRef
    return RefClass(stack, fn_name, args)


class GetAtt(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt "))
    '''
    A function for resolving resource attributes.

    Takes the form::

        { "Fn::GetAtt" : [ "<resource_name>",
                           "<attribute_name" ] }
    '''

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ __init__ "))
        super(GetAtt, self).__init__(stack, fn_name, args)

        self._resource_name, self._attribute = self._parse_args()

    def _parse_args(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ _parse_args "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ _parse_args "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ _parse_args "))
        try:
            resource_name, attribute = self.args
        except ValueError:
            raise ValueError(_('Arguments to "%s" must be of the form '
                               '[resource_name, attribute]') % self.fn_name)

        return resource_name, attribute

    def _resource(self, path='unknown'):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ _resource "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ _resource "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ _resource "))
        resource_name = function.resolve(self._resource_name)

        try:
            return self.stack[resource_name]
        except KeyError:
            raise exception.InvalidTemplateReference(resource=resource_name,
                                                     key=path)

    def dep_attrs(self, resource_name):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ dep_attrs "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ dep_attrs "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ dep_attrs "))
        if self._resource().name == resource_name:
            attrs = [function.resolve(self._attribute)]
        else:
            attrs = []
        return itertools.chain(super(GetAtt, self).dep_attrs(resource_name),
                               attrs)

    def dependencies(self, path):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ dependencies "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ dependencies "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ dependencies "))
        return itertools.chain(super(GetAtt, self).dependencies(path),
                               [self._resource(path)])

    def validate(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ validate "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ validate "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ validate "))
        super(GetAtt, self).validate()
        res = self._resource()
        attr = function.resolve(self._attribute)
        if (type(res).FnGetAtt == resource.Resource.FnGetAtt and
                attr not in res.attributes_schema.keys()):
            raise exception.InvalidTemplateAttribute(
                resource=self._resource_name, key=attr)

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class GetAtt/ result "))
        attribute = function.resolve(self._attribute)

        r = self._resource()
        if (r.action in (r.CREATE, r.ADOPT, r.SUSPEND, r.RESUME, r.UPDATE)):
            return r.FnGetAtt(attribute)
        else:
            return None


class Select(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select "))
    '''
    A function for selecting an item from a list or map.

    Takes the form (for a list lookup)::

        { "Fn::Select" : [ "<index>", [ "<value_1>", "<value_2>", ... ] ] }

    Takes the form (for a map lookup)::

        { "Fn::Select" : [ "<index>", { "<key_1>": "<value_1>", ... } ] }

    If the selected index is not found, this function resolves to an empty
    string.
    '''

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select/ __init__ "))
        super(Select, self).__init__(stack, fn_name, args)

        try:
            self._lookup, self._strings = self.args
        except ValueError:
            raise ValueError(_('Arguments to "%s" must be of the form '
                               '[index, collection]') % self.fn_name)

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Select/ result "))
        index = function.resolve(self._lookup)

        try:
            index = int(index)
        except (ValueError, TypeError):
            pass

        strings = function.resolve(self._strings)

        if strings == '':
            # an empty string is a common response from other
            # functions when result is not currently available.
            # Handle by returning an empty string
            return ''

        if isinstance(strings, six.string_types):
            # might be serialized json.
            try:
                strings = jsonutils.loads(strings)
            except ValueError as json_ex:
                fmt_data = {'fn_name': self.fn_name,
                            'err': json_ex}
                raise ValueError(_('"%(fn_name)s": %(err)s') % fmt_data)

        if isinstance(strings, collections.Mapping):
            if not isinstance(index, six.string_types):
                raise TypeError(_('Index to "%s" must be a string') %
                                self.fn_name)
            return strings.get(index, '')

        if (isinstance(strings, collections.Sequence) and
                not isinstance(strings, six.string_types)):
            if not isinstance(index, six.integer_types):
                raise TypeError(_('Index to "%s" must be an integer') %
                                self.fn_name)

            try:
                return strings[index]
            except IndexError:
                return ''

        if strings is None:
            return ''

        raise TypeError(_('Arguments to %s not fully resolved') %
                        self.fn_name)


class Join(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join "))
    '''
    A function for joining strings.

    Takes the form::

        { "Fn::Join" : [ "<delim>", [ "<string_1>", "<string_2>", ... ] }

    And resolves to::

        "<string_1><delim><string_2><delim>..."
    '''

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ __init__ "))
        super(Join, self).__init__(stack, fn_name, args)

        example = '"%s" : [ " ", [ "str1", "str2"]]' % self.fn_name
        fmt_data = {'fn_name': self.fn_name,
                    'example': example}

        if isinstance(self.args, (six.string_types, collections.Mapping)):
            raise TypeError(_('Incorrect arguments to "%(fn_name)s" '
                              'should be: %(example)s') % fmt_data)

        try:
            self._delim, self._strings = self.args
        except ValueError:
            raise ValueError(_('Incorrect arguments to "%(fn_name)s" '
                               'should be: %(example)s') % fmt_data)

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ result "))
        strings = function.resolve(self._strings)
        if strings is None:
            strings = []
        if (isinstance(strings, six.string_types) or
                not isinstance(strings, collections.Sequence)):
            raise TypeError(_('"%s" must operate on a list') % self.fn_name)

        delim = function.resolve(self._delim)
        if not isinstance(delim, six.string_types):
            raise TypeError(_('"%s" delimiter must be a string') %
                            self.fn_name)

        def ensure_string(s):
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ ensure_string "))
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ ensure_string "))
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Join/ ensure_string "))
            if s is None:
                return ''
            if not isinstance(s, six.string_types):
                raise TypeError(
                    _('Items to join must be strings %s') % (repr(s)[:200]))
            return s

        return delim.join(ensure_string(s) for s in strings)


class Split(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split "))
    '''
    A function for splitting strings.

    Takes the form::

        { "Fn::Split" : [ "<delim>", "<string_1><delim><string_2>..." ] }

    And resolves to::

        [ "<string_1>", "<string_2>", ... ]
    '''

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split/ __init__ "))
        super(Split, self).__init__(stack, fn_name, args)

        example = '"%s" : [ ",", "str1,str2"]]' % self.fn_name
        fmt_data = {'fn_name': self.fn_name,
                    'example': example}

        if isinstance(self.args, (six.string_types, collections.Mapping)):
            raise TypeError(_('Incorrect arguments to "%(fn_name)s" '
                              'should be: %(example)s') % fmt_data)

        try:
            self._delim, self._strings = self.args
        except ValueError:
            raise ValueError(_('Incorrect arguments to "%(fn_name)s" '
                               'should be: %(example)s') % fmt_data)

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Split/ result "))
        strings = function.resolve(self._strings)

        if not isinstance(self._delim, six.string_types):
            raise TypeError(_("Delimiter for %s must be string") %
                            self.fn_name)
        if not isinstance(strings, six.string_types):
            raise TypeError(_("String to split must be string; got %s") %
                            type(strings))

        return strings.split(self._delim)


class Replace(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace "))
    '''
    A function for performing string substitutions.

    Takes the form::

        { "Fn::Replace" : [
            { "<key_1>": "<value_1>", "<key_2>": "<value_2>", ... },
            "<key_1> <key_2>"
          ] }

    And resolves to::

        "<value_1> <value_2>"

    This is implemented using python str.replace on each key. The order in
    which replacements are performed is undefined.
    '''

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ __init__ "))
        super(Replace, self).__init__(stack, fn_name, args)

        self._mapping, self._string = self._parse_args()

        if not isinstance(self._mapping, collections.Mapping):
            raise TypeError(_('"%s" parameters must be a mapping') %
                            self.fn_name)

    def _parse_args(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ _parse_args "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ _parse_args "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ _parse_args "))

        example = ('{"%s": '
                   '[ {"$var1": "foo", "%%var2%%": "bar"}, '
                   '"$var1 is %%var2%%"]}' % self.fn_name)
        fmt_data = {'fn_name': self.fn_name,
                    'example': example}

        if isinstance(self.args, (six.string_types, collections.Mapping)):
            raise TypeError(_('Incorrect arguments to "%(fn_name)s" '
                              'should be: %(example)s') % fmt_data)

        try:
            mapping, string = self.args
        except ValueError:
            raise ValueError(_('Incorrect arguments to "%(fn_name)s" '
                               'should be: %(example)s') % fmt_data)
        else:
            return mapping, string

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ result "))
        template = function.resolve(self._string)
        mapping = function.resolve(self._mapping)

        if not isinstance(template, six.string_types):
            raise TypeError(_('"%s" template must be a string') % self.fn_name)

        if not isinstance(mapping, collections.Mapping):
            raise TypeError(_('"%s" params must be a map') % self.fn_name)

        def replace(string, change):
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ replace "))
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ replace "))
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Replace/ replace "))
            placeholder, value = change

            if not isinstance(placeholder, six.string_types):
                raise TypeError(_('"%s" param placeholders must be strings') %
                                self.fn_name)

            if value is None:
                value = ''

            if not isinstance(value,
                              (six.string_types, six.integer_types,
                               float, bool)):
                raise TypeError(_('"%s" params must be strings or numbers') %
                                self.fn_name)

            return string.replace(placeholder, unicode(value))

        return reduce(replace, six.iteritems(mapping), template)


class Base64(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Base64 "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Base64 "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Base64 "))
    '''
    A placeholder function for converting to base64.

    Takes the form::

        { "Fn::Base64" : "<string>" }

    This function actually performs no conversion. It is included for the
    benefit of templates that convert UserData to Base64. Heat accepts UserData
    in plain text.
    '''

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Base64/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Base64/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class Base64/ result "))
        resolved = function.resolve(self.args)
        if not isinstance(resolved, six.string_types):
            raise TypeError(_('"%s" argument must be a string') % self.fn_name)
        return resolved


class MemberListToMap(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap "))
    '''
    A function for converting lists containing enumerated keys and values to
    a mapping.

    Takes the form::

        { 'Fn::MemberListToMap' : [ 'Name',
                                    'Value',
                                    [ '.member.0.Name=<key_0>',
                                      '.member.0.Value=<value_0>',
                                      ... ] ] }

    And resolves to::

        { "<key_0>" : "<value_0>", ... }

    The first two arguments are the names of the key and value.
    '''

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ __init__ "))
        super(MemberListToMap, self).__init__(stack, fn_name, args)

        try:
            self._keyname, self._valuename, self._list = self.args
        except ValueError:
            correct = '''
            {'Fn::MemberListToMap': ['Name', 'Value',
                                     ['.member.0.Name=key',
                                      '.member.0.Value=door']]}
            '''
            raise TypeError(_('Wrong Arguments try: "%s"') % correct)

        if not isinstance(self._keyname, six.string_types):
            raise TypeError(_('%s Key Name must be a string') % self.fn_name)

        if not isinstance(self._valuename, six.string_types):
            raise TypeError(_('%s Value Name must be a string') % self.fn_name)

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ result "))
        member_list = function.resolve(self._list)

        if not isinstance(member_list, collections.Iterable):
            raise TypeError(_('Member list must be a list'))

        def item(s):
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ item "))
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ item "))
            LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class MemberListToMap/ item "))
            if not isinstance(s, six.string_types):
                raise TypeError(_("Member list items must be strings"))
            return s.split('=', 1)

        partials = dict(item(s) for s in member_list)
        return aws_utils.extract_param_pairs(partials,
                                             prefix='',
                                             keyname=self._keyname,
                                             valuename=self._valuename)


class ResourceFacade(function.Function):
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade "))
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade "))
    '''
    A function for obtaining data from the facade resource from within the
    corresponding provider template.

    Takes the form::

        { "Fn::ResourceFacade": "<attribute_type>" }

    where the valid attribute types are "Metadata", "DeletionPolicy" and
    "UpdatePolicy".
    '''

    _RESOURCE_ATTRIBUTES = (
        METADATA, DELETION_POLICY, UPDATE_POLICY,
    ) = (
        'Metadata', 'DeletionPolicy', 'UpdatePolicy'
    )

    def __init__(self, stack, fn_name, args):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade/ __init__ "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade/ __init__ "))
        super(ResourceFacade, self).__init__(stack, fn_name, args)

        if self.args not in self._RESOURCE_ATTRIBUTES:
            fmt_data = {'fn_name': self.fn_name,
                        'allowed': ', '.join(self._RESOURCE_ATTRIBUTES)}
            raise ValueError(_('Incorrect arguments to "%(fn_name)s" '
                               'should be one of: %(allowed)s') % fmt_data)

    def result(self):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade/ result "))
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/cfn/functions.py/Class ResourceFacade/ result "))
        attr = function.resolve(self.args)

        if attr == self.METADATA:
            return self.stack.parent_resource.metadata_get()
        elif attr == self.UPDATE_POLICY:
            up = self.stack.parent_resource.t.get('UpdatePolicy', {})
            return function.resolve(up)
        elif attr == self.DELETION_POLICY:
            dp = self.stack.parent_resource.t.deletion_policy()
            return function.resolve(dp)
