class LFU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = {}
        self.page_faults = 0

    def check_page_in_cache(self, page):
        was_page_fault = False

        if page in self.pages:
            self.pages[page] += 1
        else:
            if len(self.pages) < self.capacity:
                self.pages[page] = 1
                self.page_faults += 1

                was_page_fault = True
            else:
                min_page = min(self.pages, key=self.pages.get)
                del self.pages[min_page]
                self.pages[page] = 1
                self.page_faults += 1

                was_page_fault = True

        return was_page_fault