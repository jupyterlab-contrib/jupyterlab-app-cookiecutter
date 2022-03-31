const baseConfig = require('@jupyterlab/galata/lib/playwright-config');

module.exports = {
  ...baseConfig,
  use: {
    baseURL: 'http://localhost:8866',
    video: 'retain-on-failure'
  },
  expect: {
    toMatchSnapshot: { threshold: 0.33 },
  },
  preserveOutput: 'failures-only',
  retries: 0
};
