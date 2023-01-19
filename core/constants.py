departments = [
    dict(
        parent_department='nursing_office',
        ar_department=(
            'الحوامل',
            'ما بعد الولادة الطبيعية',
            'ما بعد الولادة القيصرية',
            'كشك الولادة',
            'العمليات',
            "الطوارئ",
            'العنايةالمركزة لحديثي الولادة',
            'العناية المركزةللأطفال',
            'وحدة الأطفال الأصحاء',
            'العناية المركزةللكبار',
            'أمراض النساء',
            'العيادات',
            'التدريب المستمر للتمريض',
        ),
        en_department=(
            'm1',
            'm2',
            'm3',
            'dr',
            'nursing_or',
            'nursing_er',
            'nursing_nico',
            'nursing_pico',
            'healthy_baby_Unit',
            'nursing_icu',
            'gynecology',
            'opd',
            'nurse_training',
        ), ),
    dict(
        parent_department='infection_control',
        ar_department=(
            'التعقيم',
            'النفايات الطبية',
            'الصحة العامة',
        ),
        en_department=(
            'sterilization',
            'medical_waste',
            'general_health',
        ), ),
    dict(
        parent_department='medical_services',
        ar_department=(
            'النساءوالولادة',
            'العناية المركزة للكبار(أطباء)',
            'العناية المركزة للأطفال(أطباء)',
            'العناية المركزة لحديثي الولادة(أطباء)',
            'التخدير',
            'العلاج التنفسي',
            'العمليات(أطباء)',
            'باطنية الأطفال',
            'جراحة الاطفال',
            'إدارة الأسرة',
            'المراجعة الاكلينيكية',
            'الرعاية الصحية المنزلية',
        ),
        en_department=(
            'ob_gyne',
            'doctors_icu',
            'doctors_picu',
            'doctors_nicu',
            'anesthesia',
            'respiratory',
            'doctors_or',
            'esoteric_children',
            'pediatric_surgery',
            'beds_management',
            'clinical_review',
            'home_health_care',)
    ),

    dict(
        parent_department='support_medical_services',
        ar_department=(
            'الرعاية الصيدلية',
            'خدمات التغذية',
            'التغذية السريريه',
            'الاشعة',
            'المختبر و نقل الدم',
            'العلاج الطبيعي',
            'التوعية الدينية'
        ),
        en_department=(
            'pharmacy_care',
            'nutrition_services',
            'clinical_nutrition',
            'rays',
            'laboratory_and_blood_transfusion',
            'physical_therapy',
            'religious_awareness',
        )
    ),
    dict(

        parent_department='medical_supplies',

        ar_department=(

            'المستودعات الطبية',
            'المستودعات غير الطبية ',
            'التجهيزات',
            'المشتريات',
            'العقود',

        ),
        en_department=(

            'medical_warehouses',
            'non_medical_warehouses',
            'fittings',
            'purchases',
            'contracts',
        )
    ),
    dict(
        parent_department='financial_affairs',
        ar_department=(
            'الشؤون المالية',
            'الصندوق',
            'الميزانية و التخطيط',

        ),

        en_department=(
            'financial_affairs',
            'found',
            'budget',

        ),
    ),

    dict(

        parent_department='operating',
        ar_department=(

            'الهندسة الطبية الحيوية',
            'الصيانة العامة',
            'السلامة',
            'الخدمات العامة',
            'الحركة',
            'المغسلة',
            'إدارة المرافق و المشاريع',
        ),

        en_department=(

            'biomedical_Engineering',
            'general_maintenance',
            'safety',
            'general_services',
            'motivation',
            'laundry',
            'facilities_and_project_management',

        ),
    ),

    dict(
        parent_department='quality_and_patient_safety',
        en_department=('quality_and_patient_safety',),
        ar_department=('الجودة وسلامة المرضى',),
    ),

    dict(
        parent_department='corporate_communication',
        ar_department=('التواصل المؤسسي',),
        en_department=('corporate_communication',),
    ),

    dict(
        parent_department='academic_affairs_and_training',
        ar_department=('الشؤون الأكاديمية و التدريب',),
        en_department=('academic_affairs_and_training',),
    ),

    dict(
        parent_department='development_and_projects',
        ar_department=('التطوير و المشاريع',),
        en_department=('development_and_projects',),
    ),

    dict(
        parent_department='revenue_development',
        ar_department=('تنمية الإرادات',),
        en_department=('revenue_development',),
    ),

    dict(
        parent_department='legal_affairs_and_compliance',
        ar_department=('الشؤون القانونية و الإلتزام',),
        en_department=('legal_affairs_and_compliance',),
    ),
    dict(
        parent_department='shift_management',
        ar_department=('الادارة المناوبة',),
        en_department=('shift_management',),
    ),
    dict(
        parent_department='patient_experience',
        en_department=('patient_experience',),
        ar_department=('تجربةالمريض',),
    ),
    dict(
        parent_department='human_resources',
        ar_department=('الموارد البشرية',),
        en_department=('human_resources',),
    ),
    dict(
        parent_department='patient_affairs',
        ar_department=('شؤون المرضى',),
        en_department=('patient_affairs',),
    ),
    dict(
        parent_department='e_health',
        ar_department=('الصحة الالكترونية',),
        en_department=('e_health',),
    ),
    dict(
        parent_department='hospital_director',
        ar_department=('مدير مستشفى الولادة و الأطفال',),
        en_department=('hospital_director',),
        hidden=True,
    ),
    dict(
        parent_department='health_security',
        ar_department=('الأمن الصحي',),
        en_department=('health_security',),
    ), dict(
        parent_department='employee_clinic',
        ar_department=('صحة العاملين',),
        en_department=('employee_clinic',),
    ),
    dict(
        parent_department='housing_management',
        ar_department=('إدارة السكن',),
        en_department=('housing_management',),
    ), dict(
        parent_department='pharmacy_dept',
        ar_department=('الصيدلية',),
        en_department=('pharmacy_dept',),
    ),
    dict(
        parent_department='assistant_medical_services',
        ar_department=('مدير الخدمات الطبية',),
        en_department=('assistant_medical_services',),
    ), dict(
        parent_department='security',
        ar_department=('الامن',),
        en_department=('security',),
    ),

    dict(
        parent_department='nursing_director',
        ar_department=('رئيس التمريض',),
        en_department=('nursing_director',),
        hidden=True,
    ),
    dict(
        parent_department='inventory_control',
        ar_department=('مراقبة المخزون',),
        en_department=('inventory_control',),

    ),
    dict(
        parent_department='financial_affairs_department',
        ar_department=('الشؤون القانونية',),
        en_department=('financial_affairs_department',),
        hidden=True,

    ),
    dict(
        parent_department='monitoring_the_regularity_of_human_resources',
        ar_department=('مراقبة انتظام دوام الموارد البشرية',),
        en_department=('monitoring_the_regularity_of_human_resources',),
        hidden=True,

    )
]
