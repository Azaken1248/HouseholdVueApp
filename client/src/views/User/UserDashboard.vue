<template>
  <div class="container mt-5" v-if="isAuthenticated">
    <h2>User Dashboard</h2>

    <!-- Service Requests Section -->
    <div class="row">
      <div class="col-md-12">
        <h3>Your Service Requests</h3>
        <table class="table">
          <thead>
            <tr>
              <th>Request ID</th>
              <th>Service</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="userServiceRequests.length === 0">
              <td colspan="4">No service requests available</td>
            </tr>
            <tr v-else v-for="request in userServiceRequests" :key="request.id">
              <td>{{ request.service_id }}</td>
              <td>{{ request.service }}</td>
              <td>{{ request.status }}</td>
              <td>
                <button class="btn btn-danger btn-sm" @click="cancelServiceRequest(request.id)">Cancel</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Buttons Section -->
    <div class="mt-4">
      <button class="btn btn-primary" @click="navigateToServiceRequestForm">Request New Service</button>
      <button class="btn btn-success btn-sm" @click="logoutUser">Logout</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: "UserDashboard",
  setup() {
    const userServiceRequests = ref([]);
    const isAuthenticated = ref(false);
    const router = useRouter();

    const fetchUserServiceRequests = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get('https://skibidi2.rrex.cc/api/service-requests', {
          headers: { Authorization: `Bearer ${token}` }
        });
        console.log(response.data);
        userServiceRequests.value = response.data;
      } catch (error) {
        console.error("Error fetching service requests:", error);
      }
    };

    const cancelServiceRequest = async (requestId) => {
  try {
    const token = localStorage.getItem('access_token');
    await axios.patch(`https://skibidi2.rrex.cc/api/service-requests/${requestId}/cancel`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    });
    // Update local data
    const request = userServiceRequests.value.find(r => r.id === requestId);
    if (request) {
      request.status = "canceled";
    }
  } catch (error) {
    console.error("Error canceling service request:", error);
  }
};

    const navigateToServiceRequestForm = () => {
      router.push({ name: 'CustomerRequests' });
    };

    const logoutUser = () => {
      localStorage.removeItem("access_token");
      isAuthenticated.value = false;
      router.push({ name: 'Login' });
    };

    onMounted(() => {
      const token = localStorage.getItem('access_token');
      if (token) {
        isAuthenticated.value = true;
        fetchUserServiceRequests();
      } else {
        router.push({ name: 'Login' });
      }
    });

    return { userServiceRequests, isAuthenticated, cancelServiceRequest, navigateToServiceRequestForm, logoutUser };
  }
};
</script>

<style scoped>
  table th {
    background-color: #073642;
    border: 1px solid #00fec3;
    color: #00fec3;
  }
  table tr td {
    background-color: #073642;
    border: 1px solid #00fec3;
    color: #00fec3;
  }
  button {
    margin: 10px;
    background-color: #073642;
    color: #00fec3;
    border-color: #00fec3;
  }
  button:hover {
    background-color: #00fec3;
    color: #073642;
  }
</style>
