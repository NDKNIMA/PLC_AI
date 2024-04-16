import json
import requests
from django.shortcuts import render
def hi(request):
    return render(request, 'index.html')
def result(request):
    return render(request, 'result.html')
def generate_code(request):
    if request.method == 'POST':
        # دریافت اطلاعات از فرم
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        digital_input_ports = request.POST.get('digital_input_ports')
        digital_output_ports = request.POST.get('digital_output_ports')
        analog_input_ports = request.POST.get('analog_input_ports')
        analog_output_ports = request.POST.get('analog_output_ports')
        custom_param = request.POST.get('custom_param')

        # تنظیم پرومپت با استفاده از اطلاعات ورودی کاربر
        prompt='hi'
        #prompt = f"سلام من ی plc دارم با برند {brand} مدل {model} با{digital_input_ports} پورت مرودی دیجیتال, {digital_output_ports} پورت خروجی دیجیتال, {analog_input_ports} پورت ورودی آنالوگ {analog_output_ports} پورت خروجی. برنامه ای بنویس که {custom_param}"
        if brand=='Siemens':
            prompt=f"سلام من ی plc دارم با برند {brand} مدل {model} با{digital_input_ports} پورت مرودی دیجیتال, {digital_output_ports} پورت خروجی دیجیتال, {analog_input_ports} پورت ورودی آنالوگ {analog_output_ports} پورت خروجی. برنامه ای بنویس که {custom_param} با زبان s7"
        elif brand=='Fatek':
            prompt=f"سلام من ی plc دارم با برند {brand} مدل {model} با{digital_input_ports} پورت مرودی دیجیتال, {digital_output_ports} پورت خروجی دیجیتال, {analog_input_ports} پورت ورودی آنالوگ {analog_output_ports} پورت خروجی. برنامه ای بنویس که {custom_param} با زبان Ladder Logic"
        elif brand=='Allen-Bradley':
            prompt=f"سلام من ی plc دارم با برند {brand} مدل {model} با{digital_input_ports} پورت مرودی دیجیتال, {digital_output_ports} پورت خروجی دیجیتال, {analog_input_ports} پورت ورودی آنالوگ {analog_output_ports} پورت خروجی. برنامه ای بنویس که {custom_param} با زبان Ladder Logic"
        elif brand=='Schneider Electric':
            prompt=f"سلام من ی plc دارم با برند {brand} مدل {model} با{digital_input_ports} پورت مرودی دیجیتال, {digital_output_ports} پورت خروجی دیجیتال, {analog_input_ports} پورت ورودی آنالوگ {analog_output_ports} پورت خروجی. برنامه ای بنویس که {custom_param} با زبان Ladder Logic"
        elif brand=='Mitsubishi Electric':
            prompt=f"سلام من ی plc دارم با برند {brand} مدل {model} با{digital_input_ports} پورت مرودی دیجیتال, {digital_output_ports} پورت خروجی دیجیتال, {analog_input_ports} پورت ورودی آنالوگ {analog_output_ports} پورت خروجی. برنامه ای بنویس که {custom_param} با زبان Ladder Logic"
        elif brand=='Omron':
            prompt=f"سلام من ی plc دارم با برند {brand} مدل {model} با{digital_input_ports} پورت مرودی دیجیتال, {digital_output_ports} پورت خروجی دیجیتال, {analog_input_ports} پورت ورودی آنالوگ {analog_output_ports} پورت خروجی. برنامه ای بنویس که {custom_param} با زبان Ladder Logic"
        # تنظیم پارامترهای payload


        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiY2UxNjUwMWYtNGUyZC00Y2E4LTgxMTQtYTVjNTg1NGU1NGVlIiwidHlwZSI6ImFwaV90b2tlbiJ9.XRb7Gzb9EAG-auW2_izvdpC1F10CCxQjp_cMy8BQUv0"}

        url = "https://api.edenai.run/v2/text/code_generation"
        payload = {
            "providers": "openai",
            "prompt": "",
            "instruction": prompt,
            "temperature": 0.1,
            "max_tokens": 500,
            "fallback_providers": ""
        }

        response = requests.post(url, json=payload, headers=headers)

        result = json.loads(response.text)
        generated_text = result['openai']['generated_text']
        def text(text):
            start_index = text.find("```") + 3
            end_index = text.find("```", start_index)
            result = text[start_index:end_index]
            return(result)
        # نمایش نتیجه به کاربر
        return render(request, 'result.html', {'generated_text': prompt,'key':text(generated_text)})

    # در صورتی که متد درخواست GET باشد، فقط فرم را به کاربر نمایش دهید
    return render(request, 'generate_code_form.html')
