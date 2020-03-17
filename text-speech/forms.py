import os
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional
from google.cloud import texttospeech


class TextToSpeechForm(FlaskForm):
    """
    Create user form for submitting text for speech synthesis
    """

    # set gcloud environment credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'EkabaSandbox-6a786234f016.json'

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    # Get language list
    voice_codes_list = list(dict.fromkeys([voice.language_codes[0] for voice in voices.voices]))
    language_list = [(ind + 1, voice) for ind, voice in enumerate(voice_codes_list)]

    # Get voice gender
    voice_gender = [(1, "Male"), (2, "Female")]

    text_field = TextAreaField('Input Text', validators=[DataRequired()])
    language_options = SelectField(u'Input Language', validators=[Optional()],
                                   choices=language_list, default=12)
    gender_options = SelectField(u'Voice Gender', validators=[Optional()],
                                 choices=voice_gender, default=1)
    submit = SubmitField('Convert Text to Speech')
