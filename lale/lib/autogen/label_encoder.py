
from sklearn.preprocessing.label import LabelEncoder as SKLModel
import lale.helpers
import lale.operators
import lale.docstrings
from numpy import nan, inf

class LabelEncoderImpl():

    def __init__(self):
        self._hyperparams = {
            
        }
        self._wrapped_model = SKLModel(**self._hyperparams)

    def fit(self, X, y=None):
        if (y is not None):
            self._wrapped_model.fit(X, y)
        else:
            self._wrapped_model.fit(X)
        return self

    def transform(self, X):
        return self._wrapped_model.transform(X)
_hyperparams_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'inherited docstring for LabelEncoder    Encode labels with value between 0 and n_classes-1.',
    'allOf': [{
        'type': 'object',
        'relevantToOptimizer': [],
        'additionalProperties': False,
        'properties': {
            
        }}],
}
_input_fit_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Fit label encoder',
    'type': 'object',
    'required': ['y'],
    'properties': {
        'y': {
            'type': 'array',
            'items': {
                'type': 'number'},
            'description': 'Target values.'},
    },
}
_input_transform_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Transform labels to normalized encoding.',
    'type': 'object',
    'required': ['y'],
    'properties': {
        'y': {
            'type': 'array',
            'items': {
                'type': 'number'},
            'description': 'Target values.'},
    },
}
_output_transform_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Transform labels to normalized encoding.',
    'type': 'array',
    'items': {
        'type': 'number'},
}
_combined_schemas = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Combined schema for expected data and hyperparameters.',
    'documentation_url': 'https://scikit-learn.org/0.20/modules/generated/sklearn.preprocessing.LabelEncoder#sklearn-preprocessing-labelencoder',
    'type': 'object',
    'tags': {
        'pre': [],
        'op': ['transformer'],
        'post': []},
    'properties': {
        'hyperparams': _hyperparams_schema,
        'input_fit': _input_fit_schema,
        'input_transform': _input_transform_schema,
        'output_transform': _output_transform_schema},
}
lale.docstrings.set_docstrings(LabelEncoderImpl, _combined_schemas)
LabelEncoder = lale.operators.make_operator(LabelEncoderImpl, _combined_schemas)

