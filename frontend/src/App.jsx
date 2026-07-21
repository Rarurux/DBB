import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Login from "./pages/Login";
import MissionControl from "./pages/MissionControl";
import IncidentInvestigation from "./pages/IncidentInvestigation";
import ExecutiveReport from "./pages/ExecutiveReport";
import Simulation from "./pages/Simulation";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/mission-control"
          element={<MissionControl />}
        />

        <Route
          path="/investigation"
          element={<IncidentInvestigation />}
        />

        <Route
          path="/executive-report"
          element={<ExecutiveReport />}
        />

        <Route
          path="/simulation"
          element={<Simulation />}
        />

        <Route
          path="*"
          element={<NotFound />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;