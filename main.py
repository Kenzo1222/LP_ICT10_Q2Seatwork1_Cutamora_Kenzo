from pyscript import document

def candidate_checker(e):
    club_members = ["kenzo cutamora", "briel lagran", "kyle delacalzada ", "nick austria", "kaizen sy", ]

    f_name = document.getElementByID("first_name").value
    l_name = document.getElementByID("last_name").value
    candidate = f_name + '' + l_name 
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate} you did not get in' f'Good job! {candidate}  you got in')
            
