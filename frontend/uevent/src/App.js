import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./components/user_authentication_system/login";
import RegisterForm from "./components/user_authentication_system/registration";
import Logout from "./components/user_authentication_system/logout";
import PostClub from "./components/main_system/post_club";
import PostEventForm from "./components/main_system/post_event";
import EventRegistrationButton from "./components/detailed_system/register_event_action";
import Profile from "./components/main_system/upload_photo";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="login" element={<LoginPage />} />
        <Route path="register" element={<RegisterForm />} />
        <Route path="logout" element={<Logout />} />
        <Route path="add/club" element={<PostClub />} />
        <Route path="add/event" element={<PostEventForm />} />
        <Route path="event/:eventId" element={<EventRegistrationButton />} />
        <Route path="profile" element={<Profile />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
