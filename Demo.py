import tkinter as tk
from tkinter import messagebox

def start_contest():
    messagebox.showinfo("Start Contest", "Your unique referral link has been generated!")

def view_leaderboard():
    messagebox.showinfo("Leaderboard", "Current top referrers:\n1. @user1\n2. @user2\n3. @user3")

def invite_friends():
    messagebox.showinfo("Invite", "Share this link:\nhttps://t.me/ReferralInviteRewardBot?start=your_id")

# GUI setup
app = tk.Tk()
app.title("ReferralInviteRewardBot UI Demo")
app.geometry("400x300")

title = tk.Label(app, text="🎁 Referral Contest Dashboard", font=("Helvetica", 14, "bold"))
title.pack(pady=15)

btn_start = tk.Button(app, text="🚀 Start Contest", width=25, command=start_contest)
btn_start.pack(pady=10)

btn_invite = tk.Button(app, text="📢 Invite Friends", width=25, command=invite_friends)
btn_invite.pack(pady=10)

btn_leaderboard = tk.Button(app, text="🏆 View Leaderboard", width=25, command=view_leaderboard)
btn_leaderboard.pack(pady=10)

app.mainloop()
