from Booking.Booking import Booking

inst = Booking()
inst.implicitly_wait(5)
inst.land_first_page()
inst.enter_dest("Bayreuth")
inst.enter_dates("2024-12-04", "2024-12-28")
inst.enter_memebers(1)
inst.submit()
inst.sort_data()
inst.select_room()
inst.reserve_room()