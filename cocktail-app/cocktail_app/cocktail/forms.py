from django import forms
from datetime import datetime

EMPTY_CHOICES = (
    ('全て', '全て'),
)

BASE_CHOICES = (
    ('ジン', 'ジン'),
    ('ウォッカ', 'ウォッカ'),
    ('ラム', 'ラム'),
    ('テキーラ', 'テキーラ'),
    ('ウィスキー', 'ウィスキー'),
    ('その他', 'その他'),
)

GLASS_CHOICES = (
    ('ショート', 'ショート'),
    ('ロング', 'ロング'),
)

TECH_CHOICES = (
    ('シェーク', 'シェーク'),
    ('ステア', 'ステア'),
    ('ビルド', 'ビルド'),
)

TASTE_CHOICES = (
    ('甘', '甘'),
    ('中', '中'),
    ('辛', '辛'),
)

ALC_CHOICES = (
    ('低め', '低め'),
    ('そこそこ', 'そこそこ'),
    ('高め', '高め'),
)






class PhotoForm(forms.Form):

    image = forms.ImageField()


class SearchForm(forms.Form):

    name = forms.CharField(
        label='名前',
        max_length=128,
        widget=forms.TextInput(),
        required=False,
    )

    base = forms.ChoiceField(
        label='ベース',
        widget=forms.RadioSelect,
        choices=EMPTY_CHOICES + BASE_CHOICES,
        required=False,
        initial=['全て'],
    )

    glass = forms.ChoiceField(
        label='グラス',
        widget=forms.RadioSelect,
        choices=EMPTY_CHOICES + GLASS_CHOICES,
        required=False,
        initial=['全て'],
    )

    tech = forms.ChoiceField(
        label='テクニック',
        widget=forms.RadioSelect,
        choices=EMPTY_CHOICES + TECH_CHOICES,
        required=False,
        initial=['全て'],
    )

    alc = forms.IntegerField(
        label='度数',
        min_value=0,
        max_value=100,
        required=False,
    )

    taste = forms.ChoiceField(
        label='テイスト',
        widget=forms.RadioSelect,
        choices=EMPTY_CHOICES + TASTE_CHOICES,
        required=False,
        initial=['全て'],
    )

    material1 = forms.CharField(
        label='材料１',
        max_length=128,
        required=False,
        widget=forms.TextInput(),

    )

    material2 = forms.CharField(
        label='材料２',
        max_length=128,
        required=False,
        widget=forms.TextInput(),

    )






class RegistrationForm(forms.Form):

    name = forms.CharField(
        label='名前',
        max_length=128,
        widget=forms.TextInput(),
        required=False,
    )

    base = forms.ChoiceField(
        label='ベース',
        widget=forms.RadioSelect,
        choices=BASE_CHOICES,
        required=False,
    )

    lengh = forms.ChoiceField(
        label='グラス',
        widget=forms.RadioSelect,
        choices=GLASS_CHOICES,
        required=False,
    )

    tech = forms.ChoiceField(
        label='テクニック',
        widget=forms.RadioSelect,
        choices=TECH_CHOICES,
        required=False,
    )

    alc = forms.IntegerField(
        label='度数',
        min_value=0,
        max_value=100,
        required=False,
    )

    taste = forms.ChoiceField(
        label='テイスト',
        widget=forms.RadioSelect,
        choices=TASTE_CHOICES,
        required=False,
    )

    material1 = forms.CharField(
        label='材料１',
        max_length=128,
        required=False,
        widget=forms.TextInput(),

    )

    material2 = forms.CharField(
        label='材料２',
        max_length=128,
        required=False,
        widget=forms.TextInput(),

    )

    contents = forms.CharField(
        label='説明',
        max_length=512,
        required=False,
        widget=forms.TextInput(),

    )


    image = forms.ImageField(
        required=False,
    )



class RequestForm(forms.Form):

    taste = forms.ChoiceField(
        label='テイスト',
        widget=forms.RadioSelect,
        choices=EMPTY_CHOICES + TASTE_CHOICES,
        required=False,
        initial=['全て'],
    )

    alc = forms.ChoiceField(
        label='度数',
        widget=forms.RadioSelect,
        choices=EMPTY_CHOICES + ALC_CHOICES,
        required=False,
        initial=['全て'],
    )
