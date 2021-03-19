"""
CookieCutter Pre-Gen Hook.

See:
    https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html
"""
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"


def is_identifier(value):
    result = False
    if hasattr(value, "isidentifier"):
        result = value.isidentifier()

    return result


# -------------------------------------
# Pre-Gen Script
# -------------------------------------

print("Checking project_slug...")
assert is_identifier(PROJECT_SLUG)

print("Done!")
