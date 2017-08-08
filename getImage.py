# scrap git repo and creates image of source code text


def save_image(source_code, file_name):
    import textwrap
    from PIL import ImageDraw
    from PIL import ImageFont
    from PIL import Image

    para = textwrap.wrap(source_code, width=810)  # need improvement.

    max_w, max_h = 5600, 3200
    im = Image.new('RGB', (max_w, max_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(
        '/usr/share/fonts/TTF/DroidSans.ttf', 14)

    current_h, pad = 0, 0
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((max_w - w) / 2, current_h), line, font=font)
        current_h += h + pad

    im.save(file_name, format='PNG', subsampling=0, quality=100)
    im.show()


def clone_repo(repo_url_list, root_dir):
    import git
    import os
    for repoUrl in repo_url_list:
        git.Repo.clone_from(repoUrl, os.path.join(root_dir, repo_name(repoUrl)))


def repo_name(url):
    for i in range(len(url) - 1, -1, -1):
        if url[i] == '/':
            return url[i + 1:len(url)]


def source_files(root_dir):
    import os
    all_file = []
    for root, d, file in os.walk(root_dir):
        # need improvement
        for f in filter(lambda x: x.endswith(".java") or x.endswith(".xml") or x.endswith(".gradle"), file):
            all_file.append(os.path.join(root, f))
    return all_file


def sourcecode_text(files_list):
    out = []
    for file in files_list:
        with open(file, mode='r') as f:
            for line in f.read().split("\n"):
                if not line.lstrip().startswith("//"):
                    out.append(line.lstrip().rstrip())
    return "".join(out)


# usage
if __name__ == "__main__":
    repo_list = [
        "https://github.com/YDrall/FlashLight-API-21-",
    ]
    rootDir = "/home/me/ck"
    # clone_repo(repo_list, rootDir)
    save_image(sourcecode_text(source_files(rootDir)), "ck.png")
