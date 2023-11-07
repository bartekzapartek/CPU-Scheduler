class LRU:
    def __init__(self, capacity, pages = []):
        self.capacity = capacity
        self.pages = pages

        self.page_faults = 0

    def check_page_in_cache(self, page):
        was_page_fault = False

        if page in self.pages:
            self.pages.remove(page)
            self.pages.append(page)
        else:
            if len(self.pages) < self.capacity:
                self.pages.append(page)
                self.page_faults += 1
                was_page_fault = True
            else:
                self.pages.pop(0)
                self.pages.append(page)
                self.page_faults += 1
                was_page_fault = True

        return was_page_fault


