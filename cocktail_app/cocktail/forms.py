from django import forms
from datetime import datetime

EMPTY_CHOICES = (
    ('全てのカクテル', '全てのカクテル'),
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
        widget=forms.CheckboxSelectMultiple,
        choices=BASE_CHOICES,
        required=False,
    )

    glass = forms.ChoiceField(
        label='グラス',
        widget=forms.CheckboxSelectMultiple,
        choices=GLASS_CHOICES,
        required=False,
    )

    tech = forms.ChoiceField(
        label='テクニック',
        widget=forms.CheckboxSelectMultiple,
        choices=TECH_CHOICES,
        required=False,
    )

    alc = forms.IntegerField(
        label='度数',
        min_value=0,
        max_value=100,
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
