#!/usr/bin/env python
# coding= utf-8
from django import template
from templateutils.utils import decode_tag_arguments, parse_tag_argument

register = template.Library()

class ForRangeNode(template.Node):
    def __init__(self, nodelist, arguments):
        self.nodelist = nodelist
        self.start = arguments["start"]
        self.stop = arguments["stop"]
        self.step = arguments["step"]
        self.separator = ''
    
    def render(self, context):
        # TODO: assign values to the context (like "for")
        output = []
        
        start = parse_tag_argument(self.start, context)
        stop = parse_tag_argument(self.stop, context)
        step = parse_tag_argument(self.step, context)
        
        for i in range(start, stop, step):
            output.append(self.nodelist.render(context))
        output = self.separator.join(output)
        return output

def forrange(parser, token):
    # TODO: add separator parameter
    default_arguments = {}
    default_arguments['start'] = 0
    default_arguments['stop'] = 0
    default_arguments['step'] = 1
    arguments = decode_tag_arguments(token, default_arguments)
    
    nodelist = parser.parse(('endforrange',))
    parser.delete_first_token()
    return ForRangeNode(nodelist, arguments)

register.tag('forrange', forrange)