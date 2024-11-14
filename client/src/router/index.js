import { createRouter, createWebHistory } from "vue-router";
import UserLogin from "../views/Auth/Login.vue";
import UserRegistration from "../views/Auth/Registration.vue";
import Dashboard from "../views/Admin/Dashboard.vue";
import UserDashboard from "../views/User/UserDashboard.vue";
import ServiceProDashboard from "../views/ServiceProfessional/ServiceProDashboard.vue";
import ManageServices from "../views/ServiceMgmt/ManageServices.vue";
import CustomerRequests from "../views/ServiceRequests/CustomerRequests.vue";
import ServiceSearch from "../views/Search/ServiceSearch.vue";

const routes = [
  
  { path: "/login/:role?", name: "Login", component: UserLogin },
  { path: "/register/:role?", name: "Registration", component: UserRegistration },
  { path: "/admin/dashboard", name: "Dashboard", component: Dashboard },
  { path: "/manage-services", name: "ManageServices", component: ManageServices },
  { path: "/customer-requests", name: "CustomerRequests", component: CustomerRequests },
  { path: "/search-services", name: "ServiceSearch", component: ServiceSearch },
  { path: "/user/dashboard", name: "UserDashboard", component: UserDashboard},
  { path: "/service/dashboard", name: "ServiceDashboard", component: ServiceProDashboard},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
