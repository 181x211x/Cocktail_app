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
