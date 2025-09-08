import requests
print('hello jobbot')
class JobBot():
    def msg_job(self, title, company, e_type, cycle, des, link, deadline):
        if e_type == "Internship":
            return self.msg_internship(title, company, cycle, des, link, deadline)
        elif e_type == "Full-time":
            return self.msg_fulltime(title, company, cycle, des, link, deadline)
        else:
            e_type = "JOB"


        cycle_line = f"\n*Cycle:* {cycle}" if cycle else ""
        deadline_line = f"\n*Apply by:* {deadline}" if deadline else ""

        return {
            "text": (
                f":sevhead: *NEW {e_type.upper()} POSTING!* :bangbang:\n"
                f"*{title}* @ {company}"
                f"{cycle_line}\n"
                f"*Desc:* {des}"
                f"{deadline_line}\n"
                f"<{link}|Apply Here>"
            )
        }

    def msg_internship(self, title, company, cycle, des, link, deadline):
        cycle_line = f"\n*Cycle:* {cycle}" if cycle else ""
        deadline_line = f"\n*Apply by:* {deadline}" if deadline else ""

        return {
            "text": (
                f":sevhead: *NEW INTERNSHIP POSTING!* :bangbang:\n"
                f"*{title}* @ {company}"
                f"{cycle_line}\n"
                f"*Desc:* {des}"
                f"{deadline_line}\n"
                f"<{link}|Apply Here>"
            )
        }

    def msg_fulltime(self, title, company, cycle, des, link, deadline):
        cycle_line = f"\n*Start Date:* {cycle}" if cycle else ""
        deadline_line = f"\n*Apply by:* {deadline}" if deadline else ""

        return {
            "text": (
                f":sevhead: *NEW FULL-TIME POSTING!* :bangbang:\n"
                f"*{title}* @ {company}"
                f"{cycle_line}\n"
                f"*Desc:* {des}"
                f"{deadline_line}\n"
                f"<{link}|Apply Here>"
            )
        }

    #posts message to given hook
    def post_msg(self, hook, msg):
        requests.post(hook, json=msg)