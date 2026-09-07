<p align="center">
  <img src="https://img.shields.io/badge/React-19.1-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React" />
  <img src="https://img.shields.io/badge/Express-5.1-000000?style=for-the-badge&logo=express&logoColor=white" alt="Express" />
  <img src="https://img.shields.io/badge/Prisma-6.8-2D3748?style=for-the-badge&logo=prisma&logoColor=white" alt="Prisma" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Socket.IO-4.8-010101?style=for-the-badge&logo=socket.io&logoColor=white" alt="Socket.IO" />
  <img src="https://img.shields.io/badge/TailwindCSS-3.4-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="TailwindCSS" />
</p>

<h1 align="center">🚗 KoPassenger</h1>

<p align="center">
  <strong>A university ride-sharing platform built for the UIU (United International University) community.</strong>
  <br />
  Connect with fellow students, share daily commutes, split travel costs, and build a greener campus network.
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-testing">Testing</a>
</p>

---

## ✨ Features

### 🧑‍💼 User Features
- **Secure Authentication** — Register, login, forgot/reset password with JWT access & refresh tokens stored in httpOnly cookies. Refresh token rotation on every use.
- **Profile Management** — Update name, email, avatar upload, change password, and account deletion with confirmation.
- **Theme Support** — Light and dark mode toggle, persisted per user.

### 🚘 Ride Sharing (One-Time Rides)
- **Post a Ride** — Organizers create one-time rides specifying route, departure time, total fare, and seat count.
- **Find a Ride** — Passengers search for available rides filtered by route and time window.
- **Join Requests & Fare Bidding** — Passengers can request to join a ride with an optional bid fare; organizers accept or reject.
- **Ride Lifecycle** — Full state machine: `OPEN → FULL → IN_PROGRESS → COMPLETED` (or `CANCELLED` at any point). Auto-rejects pending requests when a ride starts.
- **Live Dashboard** — Real-time display of active rides with countdown timers, status pills, and quick actions for both organizers and co-passengers.

### 🔁 Fixed Rides (Recurring Schedules)
- **Create Recurring Schedules** — Organizers set up weekly recurring rides by selecting days of the week and departure time.
- **Subscribe as Co-passenger** — Passengers subscribe to a fixed ride with an optional intro message; organizers accept/reject.
- **Automatic Ride Generation** — A midnight cron job auto-generates tomorrow's `RidePost` + pre-accepted `RideRequest` entries for all active schedules.
- **Pause & Toggle** — Organizers can pause/resume or delete schedules at any time.

### 💬 Real-Time Chat
- **1-on-1 Messaging** — Between ride organizer and passenger per ride request, powered by Socket.IO.
- **Group Chat** — Fixed ride participants share a group conversation linked to the schedule.
- **Conversations Page** — Unified inbox listing all active 1-on-1 and group chats with unread counts and last message preview.
- **Read Receipts** — Messages are marked as read when the chat is opened.

### ⭐ Reviews & Ratings
- **Post-Ride Reviews** — After a ride is completed, both organizers and co-passengers can rate each other (1–5 stars + optional comment).
- **Aggregate Ratings** — Each user's average rating and review count are recalculated from all reviews received.
- **Dashboard Prompts** — Passengers are nudged to review rides they recently completed.

### 🔔 Notifications
- **In-App Notifications** — Real-time bell icon with unread count for events like ride requests, acceptances, cancellations, reviews, and admin broadcasts.
- **Notification Types** — `REQUEST_JOIN`, `REQUEST_ACCEPTED`, `REQUEST_REJECTED`, `RIDE_STARTED`, `RIDE_COMPLETED`, `RIDE_CANCELLED`, `REVIEW_RECEIVED`, `ROUTINE_SUBSCRIPTION`, `ROUTINE_ACCEPTED`, `ADMIN_BROADCAST`, `ADMIN_MESSAGE`.

### 🚩 User Reporting
- **Report Users** — Any user can report another with a reason and description. Reports are queued for admin review.

### 🛡️ Admin Panel
- **Dashboard** — Platform-wide stats: users, rides, requests, messages, reviews, schedules, notifications.
- **User Management** — Search, view, suspend/unsuspend, promote/demote to admin, revoke sessions, delete accounts.
- **Ride Management** — Browse all rides with filters, admin-cancel rides with passenger notifications.
- **Schedule Management** — View and toggle all recurring ride schedules.
- **Review Moderation** — Browse and delete inappropriate reviews (with automatic rating recalculation).
- **Message Oversight** — View and delete platform messages.
- **Route Management** — CRUD for campus routes (create, update label/stops, activate/deactivate, delete unused routes).
- **Report Management** — Review user reports, update status (`PENDING → REVIEWED → RESOLVED`).
- **Broadcast Notifications** — Send platform-wide or targeted notifications to users.
- **System Health** — Database connectivity check and manual cron trigger for testing.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 19, Vite 6, React Router 7, Tailwind CSS 3, Lucide Icons, React Hook Form + Zod, Sonner (toasts), Socket.IO Client |
| **Backend** | Node.js 18+, Express 5, Prisma ORM 6, Socket.IO 4, Zod validation, Multer (uploads), Helmet, CORS, bcrypt (12 rounds) |
| **Database** | PostgreSQL (compatible with Neon serverless) |
| **Auth** | JWT (access + refresh tokens in httpOnly cookies), refresh rotation, rate limiting via `express-rate-limit` |
| **Scheduling** | `node-cron` for daily automatic ride generation |
| **Testing** | Selenium WebDriver (Python scripts for E2E browser automation) |

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** 18+
- **PostgreSQL** (local or hosted, e.g., [Neon](https://neon.tech))
- **Python 3** + Selenium (optional, for E2E tests)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/kopassenger.git
cd kopassenger
```

### 2. Install dependencies

```bash
# Install all dependencies (server + client)
npm run install:all

# Or install individually
cd server && npm install && cd ..
cd client && npm install && cd ..
```

### 3. Configure environment variables

**Server** (`server/.env`):
```env
PORT=4000
DATABASE_URL="postgresql://USER:PASSWORD@localhost:5432/kopassenger?schema=public"
JWT_ACCESS_SECRET="change-me-access-min-32-chars-long!!"
JWT_REFRESH_SECRET="change-me-refresh-min-32-chars-long!!"
FRONTEND_ORIGIN="http://localhost:5173"
NODE_ENV=development
```

**Client** (`client/.env`):
```env
# Leave empty for Vite dev proxy (recommended for development)
# VITE_API_URL=https://api.example.com
```

### 4. Set up the database

```bash
cd server
npx prisma generate
npx prisma db push
```

### 5. Seed routes and create admin user

```bash
# Seed default campus routes
node scripts/seedRoutes.js

# Create the first admin user (edit email/password in the script first)
node scripts/createAdmin.js
```

### 6. Start development servers

```bash
# From the root directory — starts both concurrently
npm run dev

# Or start individually:
npm run dev:server   # API at http://localhost:4000
npm run dev:client   # App at http://localhost:5173
```

The Vite dev server automatically proxies `/api` and `/uploads` requests to the backend, keeping cookies on the same origin.

---

## 📁 Project Structure

```
kopassenger/
├── client/                     # React frontend (Vite)
│   ├── src/
│   │   ├── api/                # API client modules (rides, routes, admin, etc.)
│   │   ├── components/         # Reusable UI components
│   │   │   └── Layout/         # AppShell, sidebar, navbar
│   │   ├── context/            # React Context providers
│   │   │   ├── AuthContext.jsx  # Auth state + token refresh
│   │   │   ├── SocketContext.jsx # Socket.IO connection
│   │   │   └── ThemeContext.jsx  # Dark/light mode
│   │   ├── pages/              # Page-level components
│   │   │   ├── admin/          # Admin panel pages (11 views)
│   │   │   ├── Dashboard.jsx   # Main user dashboard
│   │   │   ├── FindRide.jsx    # Ride search + request
│   │   │   ├── PostRide.jsx    # Create one-time / fixed rides
│   │   │   ├── MyRides.jsx     # Rides you organized
│   │   │   ├── MyRequests.jsx  # Rides you requested to join
│   │   │   ├── MyFixedRides.jsx # Recurring ride management
│   │   │   ├── Chat.jsx        # Messaging interface
│   │   │   ├── RideHistory.jsx # Completed ride history + reviews
│   │   │   └── ...             # Auth pages, profile, settings
│   │   ├── utils/              # Utility functions (time formatting)
│   │   ├── App.jsx             # Root component + routing
│   │   └── main.jsx            # Entry point
│   ├── tailwind.config.js
│   └── vite.config.js
│
├── server/                     # Express backend
│   ├── src/
│   │   ├── routes/             # API route handlers
│   │   │   ├── auth.js         # Register, login, logout, refresh, password reset
│   │   │   ├── users.js        # Profile CRUD, avatar upload, settings
│   │   │   ├── rides.js        # Ride CRUD, requests, reviews
│   │   │   ├── routines.js     # Fixed ride schedules + subscriptions
│   │   │   ├── messages.js     # 1-on-1 + group chat
│   │   │   ├── notifications.js # Notification feed
│   │   │   ├── reports.js      # User reporting
│   │   │   ├── routes.js       # Campus route listing
│   │   │   └── admin.js        # Full admin panel API
│   │   ├── middleware/         # Auth + admin middleware
│   │   ├── utils/              # Tokens, passwords, sanitization, cookies
│   │   ├── jobs/               # Cron jobs (daily ride generation)
│   │   ├── config.js           # Environment config + validation
│   │   ├── db.js               # Prisma client instance
│   │   └── index.js            # Server entry (Express + Socket.IO)
│   ├── prisma/
│   │   └── schema.prisma       # Database schema (14 models)
│   ├── scripts/                # CLI utilities
│   │   ├── createAdmin.js      # Create first admin user
│   │   ├── seedRoutes.js       # Seed default campus routes
│   │   └── migrateRoutes.js    # Route migration helper
│   └── uploads/                # User-uploaded files (avatars)
│
├── testing.py                  # Selenium E2E test (Firefox)
├── KPPrac.py                   # Selenium E2E test (Edge)
└── package.json                # Root workspace scripts
```

---

## 📚 API Reference

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/register` | Create account (sets httpOnly cookies) |
| `POST` | `/api/auth/login` | Sign in (sets httpOnly cookies) |
| `POST` | `/api/auth/logout` | Clear session cookies + revoke refresh token |
| `POST` | `/api/auth/refresh` | Rotate refresh token; returns new access + refresh cookies |
| `POST` | `/api/auth/forgot-password` | Request password reset (dev: link logged to console) |
| `POST` | `/api/auth/reset-password` | Reset password with token |

### User

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/users/me` | Get current user profile |
| `PATCH` | `/api/users/me` | Update name, email |
| `POST` | `/api/users/me/avatar` | Upload avatar (`multipart/form-data`) |
| `PATCH` | `/api/users/me/password` | Change password |
| `PATCH` | `/api/users/me/settings` | Update email notifications, theme |
| `DELETE` | `/api/users/me` | Delete account (requires `password` + `confirm: "DELETE"`) |

### Rides

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/rides` | Create a new ride |
| `GET` | `/api/rides?routeId=&fromTime=&toTime=` | Search available rides |
| `GET` | `/api/rides/public` | Public ride preview (no auth, max 6) |
| `GET` | `/api/rides/mine` | Get rides you created |
| `GET` | `/api/rides/:id` | Get ride details |
| `PATCH` | `/api/rides/:id` | Update ride (departure, fare, seats) |
| `POST` | `/api/rides/:id/request` | Request to join (optional `bidFare`) |
| `POST` | `/api/rides/:id/start` | Start ride (auto-reject pending requests) |
| `POST` | `/api/rides/:id/complete` | Mark ride as completed |
| `POST` | `/api/rides/:id/cancel` | Cancel ride (notifies passengers) |
| `GET` | `/api/rides/me/requests` | Get rides you requested to join |
| `POST` | `/api/rides/requests/:id/accept` | Accept a join request |
| `POST` | `/api/rides/requests/:id/reject` | Reject a join request |
| `POST` | `/api/rides/requests/:id/cancel` | Cancel your own request |
| `GET` | `/api/rides/:id/reviews` | Get reviews for a ride |
| `POST` | `/api/rides/:id/reviews` | Submit a review (1–5 stars + comment) |

### Fixed Rides (Routines)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/routines` | Create recurring schedule |
| `GET` | `/api/routines?routeId=` | Browse fixed rides by route |
| `GET` | `/api/routines/me` | Get your schedules (organizer + subscriber) |
| `POST` | `/api/routines/:id/subscribe` | Subscribe to a fixed ride |
| `POST` | `/api/routines/subscriptions/:id/accept` | Accept subscriber |
| `POST` | `/api/routines/subscriptions/:id/cancel` | Reject/cancel subscription |
| `PATCH` | `/api/routines/:id/toggle` | Toggle schedule active status |
| `DELETE` | `/api/routines/:id` | Delete schedule |

### Messages

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/messages/conversations` | Get all conversations (1-on-1 + group) |
| `GET` | `/api/messages/:rideRequestId` | Get 1-on-1 chat history |
| `POST` | `/api/messages/:rideRequestId` | Send 1-on-1 message |
| `PATCH` | `/api/messages/:rideRequestId/read` | Mark messages as read |
| `GET` | `/api/messages/group/:scheduleId` | Get group chat history |
| `POST` | `/api/messages/group/:scheduleId` | Send group message |

### Other

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/routes` | List campus routes |
| `GET` | `/api/notifications` | Get notification feed |
| `PATCH` | `/api/notifications/:id/read` | Mark notification as read |
| `POST` | `/api/reports` | Report a user |
| `GET` | `/api/health` | Server liveness check |

### Admin (`/api/admin/*`)

Full admin API supporting: stats, user CRUD, ride management, schedule management, review moderation, message oversight, route CRUD, report management, broadcast notifications, system health, and manual cron triggers. All endpoints require admin authentication.

---

## 🔒 Security

| Feature | Implementation |
|---------|---------------|
| **Password Hashing** | bcrypt, 12 rounds |
| **Access Token** | JWT, 15-minute TTL |
| **Refresh Token** | JWT, 7-day TTL with rotation on every refresh |
| **Cookie Security** | httpOnly, SameSite=Lax (Strict in production), Secure in production |
| **Rate Limiting** | Auth routes: 5 req/15 min per IP; Refresh: 60 req/15 min |
| **Input Validation** | Zod schemas on all endpoints + HTML/XSS sanitization |
| **CORS** | Restricted to `FRONTEND_ORIGIN` with credentials |
| **HTTP Headers** | Helmet.js security headers |
| **Account Suspension** | Admins can suspend users, immediately revoking all sessions |

---

## 🧪 Testing

The project includes Selenium-based E2E test scripts:

```bash
# Firefox
python testing.py

# Edge
python KPPrac.py
```

These scripts automate the login → post ride → interaction flow using the Selenium WebDriver.

---

## 🗄️ Database Schema

The Prisma schema defines **14 models**:

| Model | Description |
|-------|-------------|
| `User` | Core user profile with ratings, role, suspension status |
| `RefreshToken` | JWT refresh token store with rotation |
| `PasswordResetToken` | Hashed password reset tokens with expiry |
| `Route` | Campus travel routes with stops |
| `RidePost` | One-time ride postings with status lifecycle |
| `RideRequest` | Join requests with bid fare and status |
| `Review` | Post-ride reviews with 1–5 star ratings |
| `Notification` | In-app notification system |
| `Message` | 1-on-1 chat messages per ride request |
| `RideSchedule` | Recurring ride definitions (days + time) |
| `ScheduleSubscriber` | Subscriptions to recurring rides |
| `ScheduleMessage` | Group chat messages for fixed rides |
| `Report` | User-reported issues with status tracking |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📝 License

This project was built as a **Software Lab** course project at [United International University (UIU)](https://www.uiu.ac.bd/).

---

<p align="center">
  Built with ❤️ for the UIU Community
</p>
