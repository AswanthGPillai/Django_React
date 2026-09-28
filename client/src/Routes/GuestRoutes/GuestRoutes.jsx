import React from 'react'
import { Route, Routes } from 'react-router'
import { Homepage } from '../../Guest/Homepage/Homepage'
import UserRegistration from '../../Guest/UserRegistration/UserRegistration'
import Login from '../../Guest/Login/Login'

const GuestRoutes = () => {
  return (
    <div>
         <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="/user" element={<UserRegistration />} />
                <Route path="/login" element={<Login />} />
            </Routes>

    </div>
  )
}

export default GuestRoutes