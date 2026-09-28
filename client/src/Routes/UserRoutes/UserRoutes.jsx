import React from 'react'
import { Route, Routes } from 'react-router'
import Homepage from '../../User/Homepage'
import MyProfile from '../../User/MyProfile'
import EditProfile from '../../User/EditProfile'
import ChangePassword from '../../User/ChangePassword'

const UserRoutes = () => {
  return (
    <div>
        <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="/myprofile" element={<MyProfile />} />
                <Route path="/editprofile" element={<EditProfile />} />
                <Route path="/changepassword" element={<ChangePassword />} />
            </Routes>
    </div>
  )
}

export default UserRoutes