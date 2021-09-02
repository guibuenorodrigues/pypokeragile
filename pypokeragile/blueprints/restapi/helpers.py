from flask import jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect


def redirect_view(view_func_name, error=False, **kwargs):
    return redirect(url_for(view_func_name, **kwargs))


def prepare_response_json(
    status_code,
    resource_name=None,
    json_content=None,
    error_content=None,
    message=None,
    content_name = None,
    content_name_extra = None,
    json_content_extra = None,
):

    content = {}
    content['status_code'] = status_code

    if message is not None:
        content['message'] = message

    if json_content is not None:
        c_name = content_name if content_name is not None else 'content'
        content[c_name] = json_content

    if error_content is not None:
        content['error'] = error_content

    if json_content_extra is not None:
        extra_name = f'_{content_name_extra}' if content_name_extra is not None else '_extra_details'
        content[extra_name] = json_content_extra



    if resource_name is not None:
        content['resource_name'] = resource_name



    return jsonify(content), status_code
