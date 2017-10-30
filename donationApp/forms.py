from django import forms


class FoodItemForm(forms.Form):
    """
    Form for individual food item-quantity association
    """

    food_name=forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'title':'Type of Food'
        }),
        required=True,
        help_text='e.g: Rice, Roti, Raita etc.'
    )

    food_quantity= forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'title':'Quanity of Food'
        }),
        required=True,
        help_text='(kg/no of bowls/numbers)'
    )

class DonorDetailsForm(forms.Form):
    """
    Complete form for donation
    """
    def __init__(self,*args,**kwargs):
        self.user=kwargs.pop('user',None)
        super(DonorDetailsForm,self).__init__(*args,**kwargs)
        self.fields['donor_name']=forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                'title':'Name'
            }),
            initial=self.user.name,
            required=True
        )

        self.fields['donor_address']=forms.CharField(
            max_length=1000,
            widget=forms.Textarea(attrs={
                'title':'Address to collect donation'
            }),
            initial=self.user.address,
            required=True
        )

        self.fields['donor_contact']=forms.IntegerField(widget=forms.NumberInput(attrs={
            'title':'Contact No'
        }),initial=self.user.contact_no,required=True)

