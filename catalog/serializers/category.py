import settings

def serialize_categories(categoriesItem):
    category = {
        "name": categoriesItem.name,
        "display_name": categoriesItem.display_name,
        "slug": categoriesItem.slug,
        "created_at": categoriesItem.created_at,
        "updated_at": categoriesItem.updated_at,
        "categoryID": categoriesItem.id,
        "id": categoriesItem.id,
        "url": categoriesItem.slug + "-" + str(categoriesItem.id)
    }
    return category


def categories_parser(categoryQuerySet):
    categories = []

    for i in range(len(categoryQuerySet)):
        categories.append(serialize_categories(categoryQuerySet[i]))

    return categories
