def weasyprint(html: str) -> bytes:
    print(wiki_page.title)
    #https://stackoverflow.com/a/72796798
    #HTML('wiki_page.html').write_pdf(f'{wiki_page.title}.pdf')
    css = CSS(string='@page {size: A4 ;} html, body {font-size: 100%;} table { font-size: 0.8em } th, td { padding: 0.1px }')
    HTML(f'{wiki_page.url}').write_pdf(f'{wiki_page.title}.pdf', stylesheets=[css])


def prince(html: str) -> bytes:
    #using Prince
    #import subprocess, install Prince, 
    # add bin to system vaiables path check with prince --version
    #.figure, table {break-inside: auto} h3, h4, div, span, p, li, ul, a {orphans: 3; widows: 3}
    print(wiki_page.title)
    with open("styles.css", "w") as file:
        file.write('@page {size: A4; margin: 2.54cm; prince-shrink-to-fit: auto}')
    url = f"{wiki_page.url}"
    output_file = "output.pdf"
    #run prince or prince-books
    subprocess.run(["prince", url, "-s", "styles.css", "-o", output_file])