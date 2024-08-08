import requests

# GitHub Names of members
members = [
    "Maxoso41",
    "Jyods",
    "Egomann88",
    "dominictosku"
]

readme_path = "../README.md"

# README Header
readme_content = """
# Freundschaft-ist-Magie

## Disclaimer

**Wir gehören nicht zu HASBRO und sind nicht Teil der Marken "MY LITTLE PONY", "FRIENDSHIP IS MAGIC" oder ähnlichen.**  
Unser Projekt steht in keiner Verbindung zu diesen Marken. Wenn du nach offiziellen Informationen oder Inhalten zu "My Little Pony" oder "Friendship is Magic" suchst, wende dich bitte direkt an die offiziellen Kanäle von HASBRO.

## Über uns

Wir sind eine kleine Gruppe von _Freunden_, die gelegentlich an kleineren Projekten arbeitet. Diese Projekte werden manchmal öffentlich gemacht, wobei der Fokus auf Kreativität und gemeinsamer Freude liegt. Unser Ziel ist es, durch die Arbeit an diesen Projekten _Freundschaft_ und _Magie_ im digitalen Raum zu fördern.

## Mitglieder
| Bild | Name | GitHub | Webseite |
|------|------|--------|----------|
"""

# GitHub API call for member info
for username in members:
    response = requests.get(f"https://api.github.com/users/{username}")
    data = response.json()
    
    name = data.get("name", username)
    bio = data.get("bio", "")
    avatar_url = data["avatar_url"]
    github_url = f"https://github.com/{username}"
    
    # Website-URL if available
    blog_url = data.get("blog", "")
    blog_link = f"[![Website](https://img.shields.io/badge/Website-000000?style=flat&logo=web&logoColor=white)]({blog_url})" if blog_url else "-"

    # Bio text, if available
    bio_text = f" - {bio}" if bio else ""

    readme_content += f"| ![{name}]({avatar_url}) | {name}{bio_text} | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)]({github_url}) | {blog_link} |\n"

# Update README
with open(readme_path, "w", encoding="utf-8") as readme_file:
    readme_file.write(readme_content)
