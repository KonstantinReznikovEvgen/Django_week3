import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'week3.settings'
django.setup()

from jobsite.models import Vacancy, Company, Specialty

if __name__ == '__main__':

    specialty_frontend = Specialty(
        code="frontend",
        title="Фронтенд",
        picture="specty_frontend.png",
    )
    specialty_frontend.save()

    specialty_backend = Specialty(
        code="backend",
        title="Бэкэнд",
        picture="specty_backend.png",
    )
    specialty_backend.save()

    specialty_gamedev = Specialty(
        code="gamedev",
        title="Геймдев",
        picture="specty_gamedev.png",
    )
    specialty_gamedev.save()

    specialty_devops = Specialty(
        code="devops",
        title="Девопс",
        picture="specty_devops.png",
    )
    specialty_devops.save()

    specialty_design = Specialty(
        code="design",
        title="Дизайн",
        picture="specty_design.png",
    )
    specialty_design.save()

    specialty_products = Specialty(
        code="products",
        title="Продукты",
        picture="specty_products.png",
    )
    specialty_products.save()

    specialty_management = Specialty(
        code="management",
        title="Менеджмент",
        picture="specty_management.png",
    )

    specialty_testing = Specialty(
        code="testing",
        title="Тестирование",
        picture="specty_testing.png",
    )

    company_workiro = Company(
        id="1",
        name="Workiro",
        logo="logo1.png",
        employee_count="10",
        location="Новосибирск",
        description="Разрабатываем мобильные приложения и сервисы для сферы онлайн-обучения."
    )
    company_workiro.save()

    comapany_rebelrage = Company(
        id="2",
        name="Rebel Rage",
        logo="logo2.png",
        employee_count="24",
        location="Москва",
        description="Мобильные сервисы, программное обеспечение, веб-сайты, мобильные приложения."
    )
    comapany_rebelrage.save()

    company_staffingsmarter = Company(
        id="3",
        name="Staffing Smarter",
        logo="logo3.png",
        employee_count="123",
        location="Москва",
        description="Сервис онлайн-наблюдения за процессом сдачи экзамена с искусственным интеллектом"
    )
    company_staffingsmarter.save()

    company_evilthreat = Company(
        id="4",
        name="Evil Threath",
        logo="logo4.png",
        employee_count="36",
        location="Москва",
        description="Лидирующее в России и Восточной Европе ПО для проведения вебинаров и видео-конференций."
    )
    company_evilthreat.save()

    company_hirey = Company(
        id="5",
        name="Hirey",
        logo="logo5.png",
        employee_count="21",
        location="Воронеж",
        description="Телекоммуникационные и платежные сервисы, которые помогают развиваться бизнесам во всем мире."
    )
    company_hirey.save()

    company_swiftattack = Company(
        id="6",
        name="Swift Attack",
        logo="logo6.png",
        employee_count="79",
        location="Москва",
        description="Разработка сложных веб-сервисов и мобильных приложений"
    )
    company_swiftattack.save()

    company_troller = Company(
        id="7",
        name="Troller",
        logo="logo7.png",
        employee_count="230",
        location="Санкт-Петербург",
        description="Мобильное приложение, позволяющее примерить обувь и выбрать идеальную пару всего в 3 клика"
    )
    company_troller.save()

    company_primalassault = Company(
        id="8",
        name="Primal Assault",
        logo="logo8.png",
        employee_count="13",
        location="Москва",
        description="Реализуем проекты любой сложности в digital-сфере"
    )
    company_primalassault.save()

    job_python = Vacancy(
        title="Разработчик на Python",
        specialty=specialty_backend,
        company=company_staffingsmarter,
        salary_min=100000,
        salary_max=150000,
        published_at="2020-03-11",
        skills="Python, Nginx, Git, Django, Docker, Kubernetes, Высоконагруженные системы",
        description="<p>Офис в центре города с террасой и кальяном, чай, плюшки и виски всегда "
                    "в наличии. Возможен свободный график работы.</p> <p><b>Минимальные требования "
                    "это:</b></p> <ul> <li>Иметь опыт коммерческой разработки от 3-х лет</li> "
                    "<li>Умение писать Unit-тесты на свой код</li> <li>Техническое образование, особенно "
                    "приветствуем матмех и радиофак</li> <li>Знание Django, Django Rest Framework и Celery</li>"
                    " <li>Знания в развертывании кластеров</li> <li>Готовность изучать технологии передачи "
                    "видеоданных</li> </ul> <p><b>Бонусы:</b></p> <ul> <li>Официальное оформление по ТК</li> "
                    "<li>Офис в центре города</li> <li>Гибкий граф"
                    "ик</li> <li>Обучение, конференции за счет компании</li> <"
                    "li>ДМС</li> </ul> <p><b>Будет преимуществом:</b></p> <ul> <li>Опыт работы с Docker</li> <li>Навык "
                    "нап"
                    "исания сервисов на Asyncio</li> <li>Навык использ"
                    "ования командной строки Linux/UNIX</li> <li>Умение "
                    "работать с Git</li> </ul> <p>Зарплата достойная, обсуждается персонально с учетом пожеланий "
                    "на собеседовании, исходя из уровня компетенций.</p>"
    )
    job_python.save()

    job_django = Vacancy(
        id="2",
        title="Разработчик в проект на Django",
        specialty=specialty_backend,
        company=company_swiftattack,
        salary_min="80000",
        salary_max="90000",
        published_at="2020-03-11",
        skills="Python, Django, PostgreSQL",
        description="<p>Мы работаем на рынке веб-разработки уже более 10 лет. О"
                    "сновное направление - заказная разработка"
                    " веб-сервисов и разработка собственных стартапов.</p> <p><b"
                    ">Мы подойдем друг другу, если:</b></p> <ul> <"
                    "li>вы хорошо разбираетесь в Python и Django, опыт работы от 3-х лет, п"
                    "ринимали участие как минимум в нескольких пр"
                    "оектах, работали в команде.</li> <li>вы хотите работать в компании"
                    " единомышленников среди Django-разработчиков.</li>"
                    " <li>вам интересно работать над стартапами, участвовать в жиз"
                    "ни их становления</li> <li>вы не любите бюрократию"
                    ", планерки, митапы, презентации, совещания и пр. вещи, которые"
                    " отвлекают от работы</li> <li>вы жаворонок, потому ч"
                    "то знаете, что утром голова работает лучше и задачи решаются"
                    " быстрее</li> <li>вы уже знаете, что идеальных ТЗ не бывает</l"
                    "i> <li>вы понимаете, что прежде чем отдать задачу "
                    "на проверку тестировщику надо самим все хорошо проверить. А если у"
                    " проекта нет тестировщика (что периодически бы"
                    "вает), то проверить все дважды.</li> <li>вы понимаете, чт"
                    "о нужно соблюдать баланс между качеством кода и длитель"
                    "ностью разработки</li> <li>вы любите делиться знаниями, не боитесь "
                    "обращаться за помощью к коллегам</li> <li>вы "
                    "самостоятельный и ответственный, умеете здраво оценивать "
                    "свои силы</li> </ul> <p><b>Как у нас все устроено:</b><"
                    "/p> <ul> <li>в качестве мессенджера Slack</li> <li>ведение задач в"
                    " Gitlab</li> <li>таймтрекинг в Toggl</li> <li>"
                    "проекты завернуты в Docker</li> <li>CI/CD настроен</li> <l"
                    "i>Тесты пишем редко (только ключевой функционал покрыв"
                    "аем при необходимости)</li></ul> <p><b>Что предлагаем:</b></p> <ul> <li>Ст"
                    "абильную удаленную работу</li> <li>Про"
                    "ектную работу/Официальное трудоустройство</li> <li>Почасов"
                    "ую оплату/Оплату за месяц</li> <li>Обсуждаемое количес"
                    "тво рабочих часов в месяц (100-200)</li> <li>Регулярные выплат"
                    "ы (2 раза в месяц)</li> <li>Лояльный рабочий графи"
                    "к, начало рабочего дня не позже 10 по мск</li> <li>Интересные п"
                    "роекты, сложные задачи, работа с современными тех"
                    "нологиями</li> </ul>"
    )
    job_django.save()

    job_swift = Vacancy(
        id="3",
        title="Middle SWIFT-разработчик",
        specialty=specialty_backend,
        company=company_workiro,
        salary_min="120000",
        salary_max="150000",
        published_at="2020-03-11",
        skills="Swift, CoreData, Git, ООП, Базы данных",
        description="<p>Развиваем приложение для изучения китайских слов и иероглифо"
                    "в. Хороши в контенте и дизайне, но не хватает прав"
                    "ильного разработчика/разработчиков. Наша цель — сделать "
                    "лидирующий мировой сервис для изучения китай"
                    "ского языка. В связи с чем ищем на полную или частичную"
                    " удалённую занятость Senior/Middle iOS разраб"
                    "отчика.</p> <p><b>Стек технологий:</b></p> <ul> <li>Swi"
                    "ft</li> <li>Combine</li> <li>CoreData</li> <l"
                    "i>UI Constraints</li> <li>Git</li> </ul> <p><b>Что ожид"
                    "аем от вас:</b></p> <ul> <li>студенты старших"
                    " курсов и выпускники ВУЗов по Computer Science;</li> <li>по"
                    "нимание принципов ООП;</li> <li>владение "
                    "английским языком (минимум Intermediate);</li> <li>готовность работат"
                    "ь в команде;</li> <li>инициатив"
                    "ность;</li> <li>ответственность и умение п"
                    "ланировать своё время;</li> <li>умение понимать текущие за"
                    "дачи компании;</li> <li> понимание разницы межд"
                    "у делать и сделать</li> </ul> <p>Предлагаем хорошую з"
                    "арплату по рынку.</p>"
    )
    job_swift.save()

    job_midle_python = Vacancy(
        id="4",
        title="Мидл программист на Python",
        specialty=specialty_backend,
        company=company_troller,
        salary_min="80000",
        salary_max="90000",
        published_at="2020-03-11",
        skills="Python, Docker, MySQL",
        description=" <p><b>Что ждем от кандидата:</b></p> <ul> <li>Опыт разработки на Python от 3 лет, участие в зак"
                    "онченном коммерческом проекте, умение его грамотно описать;</li> <li>Django / Flask</li> <li>Опы"
                    "т работы с 3D моделями и библиотеками для работы с ними (например Open3D) - будет преимуществом;"
                    "</li> <li>Опыт работы с типовыми библиотеками NumPy, SciPy, OpenCV (trimesh, open3d, pyvista);</"
                    "li> <li>SQL на базовом уровне;</li> <li>Понимание основных алгоритмов машинного обучения (линейн"
                    "ая регрессия, random forest, catboost, нейронные сети и других);</li> <li>Математическое образов"
                    "ание, опыт математического моделирования;</li> <li>Опыт работы с инструментами управления проект"
                    "ам.</li> </ul> <p><b>Чем будете заниматься:</b></p> <ul> <li>Оптимизация существующих методов ви"
                    "ртуальной примерки обуви и разработка новых;</li> <li>Повышение скорости и точности работы вирту"
                    "альной примерки обуви (от показателей SLA и выше);</li> <li>Использование библиотек и фреймворко"
                    "в numpy, pandas, scikit-learn, tensorflow, catboost, LightGBM, opencv;</li> <li>Разработка нейро"
                    "сетевых методов настройки виртуальной примерки обуви.</li> </ul> <p><b>Условия:</b></p> <ul> <li"
                    ">Официальное оформление согласно ТК РФ;</li> <li>Работа с новейшим оборудованием;</li> <li>Возмо"
                    "жность загранкомандировок на различные IT-семинары;</li> <li>График работы 5/2 с 9-00 до 18-00 ("
                    "работа в офисе, не удаленно);</li> <li>Дружный коллектив и современный офис;</li> <li>Возможност"
                    "ь дальнейшего карьерного роста.</li> </ul> <p>Окончательный уровень зарплаты обсуждается по итог"
                    "ам собеседования.</p>"
    )
    job_midle_python.save()

    job_accurate_python = Vacancy(
        id="5",
        title="Грамотный питон разработчик",
        specialty=specialty_backend,
        company=company_primalassault,
        salary_min="120000",
        salary_max="150000",
        published_at="2020-03-11",
        skills="Python, Django, PostgreSQL, Git",
        description="<p>Наши основные направления: e-commerce, геосервисы, мессенджеры, распознавание образов, автома"
                    "тизация, телефония и стартапы. Заказчики - крупные финансовые, IT, продуктовые компании России. "
                    "Ищем опытного фулл-тайм python-разработчика для работы над проектами нашей компании.</p> <p><b>Ч"
                    "то ждем от кандидата:</b></p> <ul> <li>Опыт коммерческой разработки на Python/Django от 2-х лет;"
                    "</li> <li>Знания SQL (Postgres);</li> <li>Опыт написания клиент-серверных приложений;</li> <li>У"
                    "мение оценивать объем и сроки работ;</li> <li>Git, системы bug tracking.</li> </ul> <p><b>Чем бу"
                    "дете заниматься:</b></p> <ul> <li>Участвовать во всём процессе разработки - от проектирования до"
                    " запуска.</li> <li>Оптимизировать работу приложения.</li> </ul> <p><b>Плюшки:</b></p> <ul> <li>О"
                    "клад от 140 000 руб на руки.;</li> <li>Удаленное сотрудничество с выстроенными процессами;</li> "
                    "<li>Оформление по ТК РФ.</li> <li>Амбициозные проекты, интересные с профессиональной точки зрени"
                    "я задачи;</li> <li>Команда профессионалов.</li> </ul> <p>В отклике обязательно сопроводительное "
                    "письмо, почему именно вы подходите на эту вакансию.</p>"
    )
    job_accurate_python.save()