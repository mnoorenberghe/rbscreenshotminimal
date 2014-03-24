from reviewboard.extensions.base import Extension, JSExtension
from reviewboard.urls import reviewable_url_names, review_request_url_names


apply_to_url_names = set(reviewable_url_names + review_request_url_names)


class ScreenshotMinimalJSExtension(JSExtension):
    model_class = 'RBScreenshotMinimal.Extension'
#    apply_to = apply_to_url_names


class RBScreenshotMinimalExtension(Extension):
    """
    """
    metadata = {
        'Name': 'rbscreenshotminimal',
    }

    js_extensions = [ScreenshotMinimalJSExtension]

    css_bundles = {
        'default': {
            'source_filenames': ['css/rbscreenshotminimal.less'],
#            'apply_to': apply_to_url_names,
        }
    }

    js_bundles = {
        'default': {
            'source_filenames': ['js/rbscreenshotminimal.js'],
#            'apply_to': apply_to_url_names,
        }
    }
