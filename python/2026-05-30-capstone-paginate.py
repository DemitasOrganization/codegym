"""
CODE GYM — 2026-05-30 — python — capstone-paginate (beginner+, runnable)
========================================================================

A normal, practical helper — the kind you write in any web app that returns
lists. An endpoint like `GET /products?page=2&per_page=20` has the FULL list in
hand and needs to (a) return just that page's slice and (b) tell the frontend
enough to draw the pager (which page, how many pages, is there a prev/next).

The pattern, plain:

    start = (page - 1) * per_page      # page is 1-based: page 1 starts at index 0
    end   = start + per_page
    page_items = items[start:end]      # slicing never errors, even past the end

    total_pages = (total + per_page - 1) // per_page   # ceil division, integer-only


EXERCISE
--------
Write `paginate(items, page, per_page)`.

  - `items`    — the full list of results.
  - `page`     — which page to return, 1-based.
  - `per_page` — how many items per page.

Return a dict describing that page:

    {
        "items":       [ ...the items on this page... ],
        "page":        page,
        "per_page":    per_page,
        "total_items": <len of the full list>,
        "total_pages": <number of pages, ceil(total_items / per_page)>,
        "has_prev":    <True if there is a page before this one>,
        "has_next":    <True if there is a page after this one>,
    }

Notes / edges:
  - Asking for a page past the end should give an empty "items" list, not an
    error (slicing handles this for free).
  - An empty `items` list has total_pages == 0 and no prev/next.
  - has_prev is "is page > 1"; has_next is "is page < total_pages".

    paginate([1, 2, 3, 4, 5], page=1, per_page=2)
    # -> {"items": [1, 2], "page": 1, "per_page": 2, "total_items": 5,
    #     "total_pages": 3, "has_prev": False, "has_next": True}
"""

import math

def paginate(items, page, per_page):
    
    items_to_display = items[(page-1)*per_page:page*per_page]
    total_pages = math.ceil(len(items) / per_page)

    page_info = {
        "items":        items_to_display,
        "page":         page,
        "per_page":     per_page,
        "total_items":  len(items),
        "total_pages":  total_pages,
        "has_prev":     (page>1),
        "has_next":     total_pages>page,
    }
    return page_info



# ============================================================
# EVALUATION CRITERIA — committed before solving. Do not edit.
# Run this file: `python3 2026-05-30-capstone-paginate.py`
# ============================================================
if __name__ == "__main__":
    tests = [
        # (items, page, per_page, expected)
        (list(range(1, 11)), 1, 3,
         {"items": [1, 2, 3], "page": 1, "per_page": 3, "total_items": 10,
          "total_pages": 4, "has_prev": False, "has_next": True}),

        (list(range(1, 11)), 2, 3,
         {"items": [4, 5, 6], "page": 2, "per_page": 3, "total_items": 10,
          "total_pages": 4, "has_prev": True, "has_next": True}),

        # last page, partially full
        (list(range(1, 11)), 4, 3,
         {"items": [10], "page": 4, "per_page": 3, "total_items": 10,
          "total_pages": 4, "has_prev": True, "has_next": False}),

        # page past the end -> empty items, still no error
        (list(range(1, 11)), 9, 3,
         {"items": [], "page": 9, "per_page": 3, "total_items": 10,
          "total_pages": 4, "has_prev": True, "has_next": False}),

        # exact fit: 6 items, 3 per page -> exactly 2 pages
        (list(range(1, 7)), 2, 3,
         {"items": [4, 5, 6], "page": 2, "per_page": 3, "total_items": 6,
          "total_pages": 2, "has_prev": True, "has_next": False}),

        # empty result set
        ([], 1, 5,
         {"items": [], "page": 1, "per_page": 5, "total_items": 0,
          "total_pages": 0, "has_prev": False, "has_next": False}),
    ]

    passed = 0
    for items, page, per_page, expected in tests:
        before = list(items)
        got = paginate(items, page, per_page)
        ok = got == expected
        mutated = items != before
        passed += ok and not mutated
        flag = "PASS" if (ok and not mutated) else "FAIL"
        extra = "" if ok else f"\n        expected {expected!r}\n        got      {got!r}"
        extra += "   (MUTATED INPUT!)" if mutated else ""
        print(f"{flag}  paginate(<{len(items)} items>, page={page}, per_page={per_page}){extra}")
    print(f"\n{passed}/{len(tests)} passed")
