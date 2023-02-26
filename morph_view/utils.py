class MainPageMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = [
            {'block': 'Главная', 'url': '#MENU'},
            {'block': 'О нас', 'url': '#ABOUT'},
            {'block': 'Пациентам', 'url': '#PATIENT'},
            {'block': 'Врачам', 'url': '#DOCTOR'},
            {'block': 'Контакты', 'url': ''},
        ]
        return context




