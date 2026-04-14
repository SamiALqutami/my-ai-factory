import os
import requests
import json
import time
from datetime import datetime

# --- الإعدادات الإبداعية ---
API_KEY = "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"
URL = "https://api.groq.com/openai/v1/chat/completions"

# 1. تصميم قالب "المحتوى المليوني" (UX/UI Design)
def get_full_template(keyword, content):
    return f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{keyword} | دليل الربح والتقنية 2026</title>
        <meta name="description" content="اكتشف أسرار {keyword} في هذا الدليل الشامل والمحدث يومياً لعام 2026.">
        <style>
            :root {{ --p: #2563eb; --s: #0f172a; --g: linear-gradient(135deg, #0f172a, #2563eb); }}
            body {{ font-family: 'Segoe UI', system-ui, sans-serif; margin: 0; background: #f1f5f9; color: #1e293b; line-height: 1.8; }}
            .hero {{ background: var(--g); color: white; padding: 80px 20px; text-align: center; border-radius: 0 0 50px 50px; shadow: 0 10px 30px rgba(0,0,0,0.2); }}
            .main-card {{ max-width: 1000px; margin: -60px auto 40px; background: white; padding: 40px; border-radius: 30px; box-shadow: 0 20px 50px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; }}
            h1 {{ font-size: 2.8rem; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }}
            .badge {{ display: inline-block; background: #38bdf8; color: #0f172a; padding: 5px 15px; border-radius: 20px; font-weight: bold; margin-bottom: 20px; }}
            table {{ width: 100%; border-collapse: collapse; margin: 30px 0; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }}
            th {{ background: #2563eb; color: white; padding: 15px; }}
            td {{ padding: 15px; border-bottom: 1px solid #f1f5f9; text-align: center; background: #fff; }}
            .faq-item {{ background: #f8fafc; padding: 20px; border-radius: 15px; margin-bottom: 15px; border-right: 8px solid #38bdf8; }}
            .footer {{ text-align: center; padding: 50px; color: #94a3b8; font-size: 0.9rem; }}
            .analytics-demo {{ background: #0f172a; color: #10b981; padding: 10px; border-radius: 10px; font-family: monospace; font-size: 0.8rem; text-align: center; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="hero">
            <span class="badge">تحديث حصري 2026</span>
            <h1>{keyword}</h1>
            <p>دليل شامل مدعوم بالذكاء الاصطناعي</p>
        </div>
        <div class="main-card">
            <div class="content">{content}</div>
            <div class="analytics-demo">📊 نظام تتبع نشط: جاري تحليل الزيارات من محرك بحث Google</div>
        </div>
        <div class="footer">حقوق النشر © 2026 | مصنع المحتوى الذكي | مدينة يريم - اليمن</div>
    </body>
    </html>
    """

# 2. وظيفة التوليد الذكي (Fixed Logic)
def generate_smart_content(keyword):
    prompt = f"اكتب مقالاً إبداعياً جداً لـ SEO حول '{keyword}'. استخدم لغة قوية. المقال يجب أن يحتوي على: مقدمة، جدول بيانات، خطوات عمل، وقسم FAQ. أجب بصيغة HTML (الجسد فقط) وبدون أي شرح."
    
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(URL, headers=headers, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            print(f"❌ خطأ من الخادم: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ فشل الاتصال: {e}")
        return None

# 3. محرك توليد الـ Sitemap (لجذب جوجل)
def update_sitemap(pages):
    sitemap_header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap_footer = '</urlset>'
    content = ""
    for page in pages:
        date = datetime.now().strftime("%Y-%m-%d")
        content += f"  <url>\n    <loc>https://yourdomain.com/{page}</loc>\n    <lastmod>{date}</lastmod>\n    <priority>0.80</priority>\n  </url>\n"
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_header + content + sitemap_footer)
    print("✅ تم تحديث ملف Sitemap.xml بنجاح.")

# 4. تشغيل المصنع (Main Engine)
def run_factory():
    if not os.path.exists('web_pages'): os.makedirs('web_pages')
    
    # قائمة الكلمات المستهدفة (التريندات)
    keywords = [
        "أسرار الربح من بوتات تليجرام",
        "توفير كهرباء الطاقة الشمسية في اليمن",
        "المحاسبة السحابية للمتاجر",
        "برمجة تطبيقات الذكاء الاصطناعي من الهاتف",
        "تتبع الحيتان في Binance تلقائيا"
    ]
    
    generated_files = []
    
    print("🚀 انطلاق المصنع الإبداعي V4...")
    for kw in keywords:
        print(f"🎨 جاري إبداع صفحة: {kw}")
        raw_content = generate_smart_content(kw)
        if raw_content:
            clean_html = raw_content.replace("```html", "").replace("```", "").strip()
            final_page = get_full_template(kw, clean_html)
            
            file_name = f"{kw.replace(' ', '-')}.html"
            with open(f"web_pages/{file_name}", 'w', encoding='utf-8') as f:
                f.write(final_page)
            generated_files.append(file_name)
            print(f"✅ تم.")
        time.sleep(2)
    
    update_sitemap(generated_files)
    print("\n✨ انتهى التحديث الشامل! جميع الصفحات في مجلد web_pages")

if __name__ == "__main__":
    run_factory()
