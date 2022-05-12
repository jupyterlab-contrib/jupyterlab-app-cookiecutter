const jestJupyterLab = require('@jupyterlab/testutils/lib/jest-config');

const jlabConfig = jestJupyterLab('app_data', __dirname);

const {
  moduleFileExtensions,
  moduleNameMapper,
  preset,
  setupFiles,
  transform
} = jlabConfig;

module.exports = {
  preset,
  moduleFileExtensions,
  transform,
  setupFiles,
  moduleNameMapper,
  automock: false,
  testPathIgnorePatterns: ['/lib/', '/node_modules/', 'ui-tests'],
  testRegex: '.*.spec.ts[x]?$',
  transformIgnorePatterns: [
    '/node_modules/(?!(@jupyterlab/.*|lib0|y\\-protocols|y\\-websocket|yjs)/)'
  ],
  globals: {
    'ts-jest': {
      tsconfig: '<rootDir>/tsconfig.json'
    }
  }
};
