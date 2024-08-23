token = 'TiPPUbj4qRWfKQJ'


TEST = [
    {
        "text": "animals",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["dog", "dogs", "dog1"],
        "info": {"wolf": ["grey", "power"]}
    },
    {
        "text": "How to you a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "shrek"],
        "info": {"password": ["new_password", "wrong_password"]}
    },
    {
        "text": "Pops",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["rap", "jazz", "rock"],
        "info": {"secrets": ["drive", "extremal"]}
    },
    {
        "text": "How to you a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["password", "shrek"],
        "info": {"password": ["new_password", "wrong_password"]}
    }
],

UPDATE_TEST = [{
        "id": 300,
        "text": "Updated meme",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated", "meme"],
        },
        {
        "id": "new_mem_id",
        "text": "Updated meme",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated", "meme"],
        }]

NEGATIVE_TEST = [
    {
        "text": "Updated - How to enter a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"222222222": ["22222222222222", "3333333333333333"]}
    },
    {
        "id": -0.565,
        "text": " enter a password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"4444444444444": ["33333333333", "9999999999"]}
    },
    {
        "id": None,
        "text": "Updated  password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"00000000000000": ["44444444444444444", "77777777777"]}
    },
    {
        "id": "string",
        "text": "Updated  password",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"33333333": ["33333333333", "111111111111111"]}
    },
    {
        "id": 1,
        "text": 123,
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"5555555555": ["555555555555", "55555555555555"]}
    }
]

